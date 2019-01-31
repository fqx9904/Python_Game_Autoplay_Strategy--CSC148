"""
Superclass Game
"""
from typing import Any
from game_state_1 import GameState


class Game:
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        raise NotImplementedError

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        raise NotImplementedError

    def is_over(self, state: GameState) -> bool:
        """
        Return whether or not this game is over at state.
        """
        raise NotImplementedError

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        raise NotImplementedError

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        raise NotImplementedError


class StonehengeGame(Game):
    """
    A stonehenge game to be played by two players.
    """

    def __init__(self, p1_starts: bool, side: int = None) -> None:
        """
        Initialize a stonehenge game.

        Overrides Game.__init__
        """
        self.side = input('Enter a size for the stonehenge:') \
            if not side else side
        while not self.side.isdigit():
            self.side = input('Enter a size for the stonehenge:')
        self.current_state = StonehengeState(p1_starts, int(self.side))

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.

        Overrides Game.get_instructions()
        """
        return 'Players take turns claiming cells.\nWhen a player captures at '\
               'least half of the cells in a ley-line, then the player '\
               'captures that ley-line.\nThe first player to capture at least '\
               'half of the ley-lines is the winner.\nA ley-line, once '\
               'claimed, cannot be taken by the other player.'

    def is_over(self, state: Any) -> bool:
        """
        Return whether or not this game is over at state.

        Overrides Game.is_over()
        """
        return state.p1 >= (int(self.side) + 1) * 3 / 2 or state.p2 >= \
            (int(self.side) + 1) * 3 / 2

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        Overrides Game.is_winner()
        """
        if self.is_over(self.current_state):
            return self.current_state.p1 > self.current_state.p2 \
                if player == 'p1' else self.current_state.p2 > \
                self.current_state.p1
        return False

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.

        Overrides Game.str_to_move()
        """
        return 1 if not string.isalpha() else string.upper()


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
