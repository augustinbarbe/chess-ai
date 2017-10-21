""" Ressources"""

import configparser
from redis import StrictRedis

# Config object
config = configparser.ConfigParser()
config.read('chessai.cfg')

url = config.get('REDIS', 'Redis_url')


# Redis strict connection
redis = StrictRedis.from_url(url)

class RobotPlayerException(Exception):
    """Exception class of RobotPlayer"""
    pass