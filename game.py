"""
game module
"""
from typing import Any
from state import StateChopsticks, StateSubstractSquare


class Game:
    """Represent a general game that is two-player, sequencial-move, zero-sum
    and perfect-information.

    is_p1_turn - the prameter indicates whether it's the turn for p1.
    current_state - the prameter for class State.
    """
    is_p1_turn: bool
    current_state: Any

    def __init__(self, is_p1_turn: bool, current_state: Any) -> None:
        """Initialize a game.

        >>> game = Game(True, StateChopsticks(True))
        >>> game.is_p1_turn
        True
        >>> game.current_state
        It's p1's turn. ...1-1...1-1...
        """
        self.is_p1_turn, self.current_state = is_p1_turn, current_state

    def __str__(self) -> str:
        """Return a string representation of the class Game.

        >>> print(Chopsticks(True))
        This is the game: Chopsticks.
        """
        return 'This is the game: {}.'.format(self.__class__.__name__)

    def __eq__(self, other: Any) -> bool:
        """Return whether self is equivalent to other.

        >>> Chopsticks(True) == Chopsticks(False)
        False
        """
        return type(self) == type(other) and self.is_p1_turn == \
            other.is_p1_turn and self.current_state == other.current_state

    def get_instructions(self) -> str:
        """Return a string that represents the instruction of a game.
        """
        raise NotImplementedError('Subclass needed')

    def is_over(self, current_state: Any) -> bool:
        """Return True if the game is over, False otherwise.
        """
        raise NotImplementedError('Subclass needed')

    def is_winner(self, player: str) -> bool:
        """Return True if the winner of the game is player, False otherwise.
        """
        raise NotImplementedError('Subclass needed')

    def str_to_move(self, move: str) -> Any:
        """Make the string to the move that the game needed.
        """
        raise NotImplementedError('Subclass needed')


class Chopsticks(Game):
    """Represent the Game called chopsticks. Extends Game.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """Initialize the game Chopsticks.

        Extends Game.__init__

        >>> chop = Chopsticks(True)
        >>> chop.is_p1_turn
        True
        >>> chop.current_state
        It's p1's turn. ...1-1...1-1...
        """
        Game.__init__(self, is_p1_turn, StateChopsticks(is_p1_turn))

    def get_instructions(self) -> str:
        """Return a string that represents the instruction of the game
        Chopsticks.

        Over-rides Game.get_instructions()

        >>> print(Chopsticks(True).get_instructions())
        <BLANKLINE>
        1. Each of two players begins with one finger pointed up on each of \
their hands.
        2. Player A touches one hand to one of Player B's hands, increasing \
the number of fingers pointing up on Player B's hand by the number on Player \
A's hand. The numberpointing up on Player A's hand remains the same.
        3. If Player B now has five fingers up, that hand becomes  'dead' or \
unplayable. If the number of fingers should exceed five, subtract five from \
the sum.
        4. Now Player B touches one hand to one of Player A's hands, and the \
distribution of fingers proceeds as above, including the possibility of a \
'dead' hand.
        5. Play repeats steps 2 to 4 until some player has two 'dead' hands, \
thus losing.
        <BLANKLINE>
        """
        return "\n" \
               "1. Each of two players begins with one finger pointed up " \
               "on each of their hands.\n" \
               "2. Player A touches one hand to one of Player B\'s hands, " \
               "increasing the number of fingers pointing up on Player B\'s " \
               "hand by the number on Player A\'s hand. The number" \
               "pointing up on Player A\'s hand remains the same.\n" \
               "3. If Player B now has five fingers up, that hand becomes " \
               " \'dead\' or unplayable. If the number of fingers should " \
               "exceed five, subtract five from the sum.\n" \
               "4. Now Player B touches one hand to one of Player A's hands, " \
               "and the distribution of fingers proceeds as above, including " \
               "the possibility of a 'dead' hand.\n" \
               "5. Play repeats steps 2 to 4 until some player has two " \
               "'dead' hands, thus losing.\n"

    def is_over(self, current_state: Any) -> bool:
        """Return True if the current_state indicates the game Chopsticks is
        over.

        Over-rides Game.is_over(current_state)

        >>> chop = Chopsticks(True)
        >>> chop.is_over(chop.current_state)
        False
        """
        return 0 in [sum(current_state.moves[a]) for a in current_state.moves]

    def is_winner(self, player: str) -> bool:
        """Return True if the player is the winner of the game Chopsticks,
        False otherwise.

        Over-rides Game.is_winner(player)

        >>> Chopsticks(True).is_winner('p1')
        False
        """
        if sum(self.current_state.moves[1]) == 0:
            return self.is_over(self.current_state) and player == 'p2'
        return self.is_over(self.current_state) and player == 'p1'

    def str_to_move(self, move: str) -> str:
        """Make the string to the move that the game Chopsticks needed.

        Over-rides Game.str_to_move(move)

        >>> game = Chopsticks(True)
        >>> game.str_to_move('ll')
        'll'
        """
        return move


class SubstractSquare(Game):
    """Initialize the game Substract Square. Extends Game.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """Initialize the game Substract Square.

        Extends Game.__init__
        """
        Game.__init__(self, is_p1_turn, StateSubstractSquare(is_p1_turn))

    def get_instructions(self) -> str:
        """Return a string that represents the instruction of the game
        SubstractSquare.

        Over-rides Game.get_instructions()
        """
        return "\n" \
               "1. A non-negative whole number has been chosen already.\n" \
               "2. Now the player chooses some square of a positive whole " \
               "number to subtract from the value, and the chosen square " \
               "must not be larger. Then, we have a new value and the next " \
               "player chooses a square to subtract from it.\n" \
               "3. Keep alternating until the number is 0, and the player " \
               "whose starting number is 0 loses!\n"

    def is_over(self, current_state: Any) -> bool:
        """Return True if the current_state indicates the game Substract is
        over.

        Over-rides Game.is_over(current_state)
        """
        return current_state.moves == 0

    def is_winner(self, player: str) -> bool:
        """Return True if the player is the winner of the game Substract Square,
        False otherwise.

        Over-rides Game.is_winner(player)
        """
        return self.is_over(self.current_state) and \
               player != self.current_state.get_current_player_name()

    def str_to_move(self, move: str) -> int:
        """Make the string to the move that the game Chopsticks needed.

        Over-rides Game.str_to_move(move)
        """
        return int(move) if self.current_state.is_valid_move(move) else 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
