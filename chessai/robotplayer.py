""" AI application chess wrapper"""

import configparser
import secrets
from time import sleep
import os
import redis
import sys
import time

from chess import uci, Board, Move

from chessai.ressources import config, generate_id


class RobotPlayer(object):
    """ Class wrapping the chess engine """
    def __init__(self):
        self._color = os.environ.get('COLOR') == "white"   
        self._game_id = os.environ.get('GAME_ID')
        self.bot_id = secrets.token_hex(nbytes=16)
        
        #TODO : connect from config file
        self._red = redis.StrictRedis(host='redis', db=3, port=6379, password='devpassword')
        self._engine = uci.popen_engine("/usr/games/stockfish")
        self._board = Board()


    def init_game(self):
        """set everything up for gaming"""
        self._engine.uci()
        self._engine.ucinewgame()
        self._engine.position(self._board)
        self.own_id = generate_id(self._color, self._game_id)
        self.opp_id = generate_id(not self._color, self._game_id)


    def run(self):
        """continuous game """
        pubsub = self._red.pubsub()
        pubsub.subscribe([self.opp_id])

        self.info("Entering in the pubsub")
        for move in pubsub.listen():
            self.info("Incoming message")
            
            if move['type'] == 'subscribe' and move['data'] == 1:
                self.info("Init message")
                if self._color:
                    while not self._red.get(self._game_id):
                        self.info("Waiting for black")

                    self.info("Black is connected, playing first move")

                    decision, _ = self._engine.go(movetime=2000)
                    self._red.publish(self.own_id, decision.uci())
                    self._board.push(decision)
                    self.info("Move played")

                else:
                    self._red.set(self._game_id, "ready")
                    self.info("Telling white we are ready")

            else:
                self.info("Receiving move")
                self._board.push(Move.from_uci(move['data'].decode('utf8')))
                decision, _ = self._engine.go(movetime=2000)
                self._red.publish(self.own_id, decision.uci())
                self.info("Playing move")
                self._board.push(decision)


    def info(self, message):
        """just info"""
        self._red.publish('info', "[{}][{}]{}".format(time.time(), self._color, message))

    def play(self):
        self.init_game()
        self.run()