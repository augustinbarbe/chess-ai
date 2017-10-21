""" AI application chess wrapper"""

import configparser
from time import sleep

from chessai.ressources import redis

class RobotPlayer(object):
    """ Class wrapping the ai """
    
    def __init__(self, iswhite, bot_id, game_id):
        self._bot_id = bot_id
        self._iswhite = iswhite
        self._game_id = game_id


    def start(self):
        if self._iswhite:
            print('subscribing to the game_id redis pubsub')
            while True:
                print('looking at redis')
                redis.set('foo', 'bar')
                print(redis.get('foo'))
                sleep(1)