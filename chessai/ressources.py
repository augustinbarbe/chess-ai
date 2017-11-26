""" Ressources"""
import configparser
from redis import StrictRedis

# Config object
config = configparser.ConfigParser()
config.read('chessai.cfg')

# helpers
def generate_id(color, game_id):
    """generate an idenfier according to the color"""
    identifier = "{}".format("w"  * color + "b" * (not color))
    return game_id + identifier


# Exceptions
class RobotPlayerException(Exception):
    """Exception class of RobotPlayer"""
    pass