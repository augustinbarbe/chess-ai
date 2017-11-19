""" AI application chess wrapper"""

import configparser
from time import sleep
import os
from chess import uci, Board, Move

from chessai.ressources import config
import redis

class RobotPlayer(object):
    """ Class wrapping the chess engine """
    def __init__(self):
        self._color = os.environ.get('COLOR') == "white"
        
        if self._color:
            self._bot_id = os.environ.get('WHITE_ID')
            self._opponent_id = os.environ.get('BLACK_ID')
        else:
            self._opponent_id = os.environ.get('WHITE_ID')
            self._bot_id = os.environ.get('BLACK_ID')

        self._game_id = os.environ.get('GAME_ID')
        self._red = redis.StrictRedis(host='redis', db=3, port=6379, password='devpassword')


        self._engine = uci.popen_engine("/usr/games/stockfish")
        self._board = Board()

        print("init done: ", self._bot_id, self._opponent_id, self._color)
        print("color ", self._color)

    def start(self):
        """Start the player """
        self._engine.uci()
        self._engine.ucinewgame()
        self._engine.position(self._board)

        self.run()


    def run(self):
        """continuous game """
        pubsub = self._red.pubsub()
        pubsub.subscribe([self._opponent_id])
        

        for move in pubsub.listen():
            if move['type'] == 'subscribe' and move['data'] == 1:
                print('subscription done!')

                if self._color:
                    """First move for the white"""
                    decision, _ = self._engine.go(movetime=2000)
                    self._red.publish(self._bot_id, decision.uci())
                    self._board.push(decision)
                    print(self._board)
            

            else:
                print(move['data'])
                self._board.push(Move.from_uci(move['data'].decode('utf8')))
                decision, _ = self._engine.go(movetime=2000)
                self._red.publish(self._game_id, decision.uci())
                self._board.push(decision)
                print(self._board)
                return
