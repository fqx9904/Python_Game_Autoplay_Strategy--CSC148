"""strategy module"""
from typing import Any
import random


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


# TODO: Implement a random strategy.
def computer_strategy(game: Any) -> Any:
    """
    Return a move for game by randomly choosing one.
    """
    return random.choice(game.current_state.get_possible_moves())


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
