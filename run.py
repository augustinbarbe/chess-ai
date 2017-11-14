""" Runner of the application"""
import os
import configparser
import time
import redis

from chessai.robotplayer import RobotPlayer
from chessai.ressources import RobotPlayerException


def init_game(redis_conn):
    """ Initialize the game by checking in
    environment variables """


    color = os.environ.get('COLOR_BOT')
    game_id = os.environ.get('GAME_ID')
    bot_id = os.environ.get('ID_BOT')

    if None in (color, game_id, bot_id):
        raise Exception("Env. variable not set.")


    robot = RobotPlayer(color, bot_id, game_id)

    
    return robot


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read('chessai.cfg')

    redis_conn = redis.from_url("redis://:devpassword@redis:6379/2")
    
    robot = init_game(redis_conn)
    robot.run()