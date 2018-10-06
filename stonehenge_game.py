"""
A stonehenge_game module
"""
from typing import Any
from game import Game
from stonehenge_state import StonehengeState


class StonehengeGame(Game):
    """
    A stonehenge game to be played by two players.
    """

    GET_INSTRUCTION_CHECK = \
        'Players take turns claiming cells.\nWhen a player captures at least ' \
        'half of the cells in a ley-line, then the player captures that ' \
        'ley-line.\nThe first player to capture at least half of the ' \
        'ley-lines is the winner.\nA ley-line, once claimed, cannot be taken ' \
        'by the other player.'

    def __init__(self, p1_starts: bool, side: str = None
                 ) -> None:
        """
        Initialize a stonehenge game.

        Overrides Game.__init__

        >>> game = StonehengeGame(True, '1')
        >>> repr(game.current_state) == repr(StonehengeState(True, 1))
        True
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

        >>> StonehengeGame(True, '1').get_instructions() == \
        StonehengeGame.GET_INSTRUCTION_CHECK
        True
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

        >>> game = StonehengeGame(True, '1')
        >>> game.is_over(StonehengeState(True, 1).make_move('A'))
        True
        """
        return state.p1 >= (int(self.side) + 1) * 3 / 2 or state.p2 >= \
            (int(self.side) + 1) * 3 / 2

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        Overrides Game.is_winner()

        >>> game = StonehengeGame(False, '1')
        >>> game.current_state = StonehengeState(False, 1).make_move('A')
        >>> game.is_winner('p2')
        True
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

        >>> StonehengeGame(True, '1').str_to_move('a')
        'A'
        >>> StonehengeGame(True, '1').str_to_move('B')
        'B'
        >>> StonehengeGame(True, '1').str_to_move('c21')
        1
        """
        return 1 if not string.isalpha() else string.upper()


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

    import doctest
    doctest.testmod()
