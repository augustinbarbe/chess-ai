""" Ressources"""
import configparser
from redis import StrictRedis

# Config object
config = configparser.ConfigParser()
config.read('chessai.cfg')


class RobotPlayerException(Exception):
    """Exception class of RobotPlayer"""
    pass