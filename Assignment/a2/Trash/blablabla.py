"""
A module
"""
from game_interface import *
from strategy import *


if __name__ == '__main__':
    GameInterface(StonehengeGame(True, 2), recursive_minimax(StonehengeGame),
                  recursive_minimax(StonehengeGame))
