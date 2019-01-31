"""
state module
"""
from typing import Any


class State:
    """Represent the state of a general two-player, sequencial-move, zero-sum
    and perfect-information game.

    is_p1_turn - if the current turn is p1
    moves - the possible moves that current player can pick
    """
    is_p1_turn: bool
    moves: Any

    def __init__(self, is_p1_turn: bool, moves: Any) -> None:
        """Initialize a game state.

        >>> state = State(True, 'Any')
        >>> state.is_p1_turn
        True
        >>> state.moves
        'Any'
        """
        self.is_p1_turn = is_p1_turn
        self.moves = moves

    def __str__(self) -> str:
        """Return a string representation of the game state.
        """
        raise NotImplementedError('Subclass needed')

    def __repr__(self) -> str:
        """Return a informative string representation of the game state
        equivalent to self.
        """
        raise NotImplementedError('Subclass needed')

    def __eq__(self, other: Any) -> bool:
        """Return whether self is equivalent to other.

        >>> StateSubstractSquare(True, 2) == StateChopsticks(True)
        False
        """
        return type(self) == type(other) and self.is_p1_turn == \
            other.is_p1_turn and self.moves == other.moves

    def get_possible_moves(self) -> list:
        """Return the current possible moves of a general game.
        """
        raise NotImplementedError('Subclass needed')

    def is_valid_move(self, move: Any) -> bool:
        """Return True if the move that the player made is valid, otherwise
        False.
        """
        raise NotImplementedError('Subclass needed')

    def get_current_player_name(self) -> str:
        """Return the name of the current player.

        >>> StateChopsticks(False).get_current_player_name()
        'p2'
        """
        return 'p1' if self.is_p1_turn else 'p2'

    def make_move(self, move: Any):
        """Apply the move to change the current state of the game.
        """
        raise NotImplementedError('Subclass needed')


class StateChopsticks(State):
    """Represent a state of game Chopsticks; Extends State.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """Initialize game chopsticks.

        Extends State.__init__

        >>> state = StateChopsticks(True)
        >>> state.is_p1_turn
        True
        >>> state.moves
        {1: [1, 1], 2: [1, 1]}
        """
        State.__init__(self, is_p1_turn, {1: [1, 1], 2: [1, 1]})

    def __str__(self) -> str:
        """Return a string representation of the game state of Chopsticks.

        Over-rides State.__str__

        >>> state = StateChopsticks(True)
        >>> print(state)
        It's p1's turn. ...1-1...1-1...
        """
        temp_1 = "...{}-{}...{}-{}...".format\
        (self.moves[1][0], self.moves[1][1],
         self.moves[2][0], self.moves[2][1])
        temp_2 = "Game over." \
            if 0 in [sum(self.moves[a]) for a in self.moves] \
            else ("It's {}'s turn.".format('p1' if self.is_p1_turn else 'p2'))
        return temp_2 + ' ' + temp_1

    def __repr__(self) -> str:
        """Return a informative string representation of the state of game
        Chopsticks that is equivalent to self.

        Over-rides State.__repr__

        >>> state = StateChopsticks(True)
        >>> print(repr(state))
        It's p1's turn. ...1-1...1-1...
        """
        return str(self)

    def get_possible_moves(self) -> list:
        """Return the current possible moves of game Chopsticks.

        Over-rides State.get_possible_moves()

        >>> state = StateChopsticks(True)
        >>> state.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        """
        moves = ['ll', 'lr', 'rl', 'rr']
        result = [move for move in moves if self.is_valid_move(move)]
        return result

    def is_valid_move(self, move: str) -> bool:
        """Return True if the move that the player made is valid for game
        Chopsticks, otherwise False.

        Over-rides State.is_valid_move(move)

        >>> state = StateChopsticks(True)
        >>> state.is_valid_move('not valid')
        False
        """
        return move in ['ll', 'lr', 'rl', 'rr'] and \
            (not ((move == 'll' and (self.moves[1][0] * self.moves[2][0]) == 0)
                  or (move == ('lr' if self.is_p1_turn else 'rl')
                      and (self.moves[1][0] * self.moves[2][1]) == 0)
                  or (move == ('rl' if self.is_p1_turn else 'lr')
                      and (self.moves[1][1] * self.moves[2][0]) == 0)
                  or (move == 'rr'
                      and (self.moves[1][1] * self.moves[2][1]) == 0)))

    def make_move(self, move: str) -> Any:
        """Apply the move to change the current state of the game Chopsticks.

        Over-rides State.make_move()

        >>> state = StateChopsticks(True)
        >>> state.make_move('ll')
        It's p2's turn. ...1-1...2-1...
        """
        n_state = StateChopsticks(not self.is_p1_turn)
        new_moves = {1: [self.moves[1][0], self.moves[1][1]],
                     2: [self.moves[2][0], self.moves[2][1]]}
        if self.is_p1_turn:
            if move == 'll':
                new_moves[2][0] = self.moves[2][0] + self.moves[1][0]
            elif move == 'lr':
                new_moves[2][1] = self.moves[2][1] + self.moves[1][0]
            elif move == 'rl':
                new_moves[2][0] = self.moves[2][0] + self.moves[1][1]
            elif move == 'rr':
                new_moves[2][1] = self.moves[2][1] + self.moves[1][1]
        else:
            if move == 'll':
                new_moves[1][0] = self.moves[1][0] + self.moves[2][0]
            elif move == 'lr':
                new_moves[1][1] = self.moves[1][1] + self.moves[2][0]
            elif move == 'rl':
                new_moves[1][0] = self.moves[1][0] + self.moves[2][1]
            elif move == 'rr':
                new_moves[1][1] = self.moves[1][1] + self.moves[2][1]
        new_moves = {1: [num_1 % 5 for num_1 in new_moves[1]],
                     2: [num_2 % 5 for num_2 in new_moves[2]]}
        n_state.moves = new_moves
        return n_state


class StateSubstractSquare(State):
    """Represent a state of the game Substract Square. Extends State.

    Extends State.__init__
    """

    def __init__(self, is_p1_turn: bool, moves=None) -> None:
        """Initialize a state of game Substract Square.

        Extends State.__init__

        >>> state = StateSubstractSquare(True, 2)
        >>> state.is_p1_turn
        True
        >>> state.moves
        2
        """
        State.__init__(self, is_p1_turn, moves)
        if self.moves is None:
            self.moves = input('Choose a number: ')
            while not (self.moves.isdigit() and int(self.moves) >= 0):
                self.moves = input('Choose a number: ')
        self.moves = int(self.moves)

    def __str__(self) -> str:
        """Return a string representation of the game state of Chopsticks.

        Over-rides State.__str__

        >>> state = StateSubstractSquare(True, 2)
        >>> print(state)
        It's p1's turn. The number is now: 2
        """
        temp_1 = 'The number is now: {}'.format(self.moves)
        temp_2 = "Game over." if self.moves == 0 else \
            ("It's {}'s turn.".format('p1' if self.is_p1_turn else 'p2'))
        return temp_2 + ' ' + temp_1

    def __repr__(self) -> str:
        """Return a informative string representation of the state of game
        Substract Square that is equivalent to self.

        Over-rides State.__repr__

        >>> state = StateSubstractSquare(True, 2)
        >>> print(repr(state))
        It's p1's turn. The number is now: 2
        """
        return str(self)

    def get_possible_moves(self) -> list:
        """Return the current possible moves of game Substract Square.

        Over-rides State.get_possible_moves()

        >>> state = StateSubstractSquare(True, 5)
        >>> state.get_possible_moves()
        [1, 4]
        """
        return [n ** 2 for n in range(1, self.moves + 1)
                if n ** 2 <= self.moves]

    def is_valid_move(self, move: int) -> bool:
        """Return True if the move that the player made is valid for game
        Subtract Square, otherwise False.

        Over-rides State.is_valid_move(move)

        >>> state = StateSubstractSquare(True, 5)
        >>> state.is_valid_move(2)
        False
        """
        return move is not None and str(move).isdigit() and int(move) \
               in self.get_possible_moves()

    def make_move(self, move: int) -> Any:
        """Apply the move to change the current state of the game Substract
        Square.

        Over-rides State.make_move()

        >>> game = StateSubstractSquare(True, 1)
        >>> game.make_move(1)
        Game over. The number is now: 0
        """
        new_moves = self.moves - int(move)
        new_state = StateSubstractSquare((not self.is_p1_turn), new_moves)
        return new_state


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
