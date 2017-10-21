""" Runner of the application"""
import os

from chessai.robotplayer import RobotPlayer
from chessai.ressources import redis, RobotPlayerException


def init_game(redis):
    """ Initialize the game by checking in
    environment variables """

    if not os.environ.get('ID_BOT'):
        redis.set('status_last', 'bot_id_failure')
        return None

    elif not os.environ.get('COLOR_BOT'):
        redis.set('status_last', 'color_failure')
        return None
    
    elif not os.environ.get('GAME_ID'):
        redis.set('status_last', 'game_id_failure')
        return

    color = os.environ.get('COLOR_BOT') == "white"
    game_id = os.environ.get('GAME_ID')
    bot_id = os.environ.get('ID_BOT')

    try:
        robot = RobotPlayer(color, bot_id, game_id)

    except RobotPlayerException:
        redis.set('status_last','init_bot_failure')
    
    redis.set('status_last', 'init_ok')
    
    return robot


if __name__ == "__main__":

    robot = init_game(redis)
    
    if robot:
        print('toto')