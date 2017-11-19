""" Runner of the application"""
import os
import configparser
import time
import redis

from chessai.robotplayer import RobotPlayer
from chessai.ressources import RobotPlayerException



if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read('chessai.cfg')

    redis_conn = redis.from_url("redis://:devpassword@redis:6379/2")
   
    robot = RobotPlayer()
    robot.start()
    robot.run()