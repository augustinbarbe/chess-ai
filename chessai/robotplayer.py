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
        self.redis_conn = redis.from_url("redis://:devpassword@redis:6379/2")


    def run(self):
        print("Game is running")
        print(self._bot_id, self._iswhite, self._game_id)            