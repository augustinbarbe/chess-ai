""" Runner of the application"""
import os
import configparser
import time
import redis

from chessai.robotplayer import RobotPlayer
from chessai.ressources import RobotPlayerException



if __name__ == "__main__":

    robot = RobotPlayer()
    robot.play()