"""
The GameState superclass.

NOTE: You do not have to run python-ta on this file.
"""
from typing import Any
from grid import Grid


class GameState:
    """
    The state of a game at a certain point in time.

    WIN - score if player is in a winning position
    LOSE - score if player is in a losing position
    DRAW - score if player is in a tied position
    p1_turn - whether it is p1's turn or not
    """
    WIN: int = 1
    LOSE: int = -1
    DRAW: int = 0
    p1_turn: bool

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        """
        self.p1_turn = is_p1_turn

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        raise NotImplementedError

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        raise NotImplementedError

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: Any) -> 'GameState':
        """
        Return the GameState that results from applying move to this GameState.
        """
        raise NotImplementedError

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this GameState.
        """
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        raise NotImplementedError

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        raise NotImplementedError


class StonehengeState(GameState):
    """
    The state of stonehenge game at a certain point of time.

    size - the side-length of the stonehenge
    """
    size: int

    def __init__(self, is_p1_turn: bool, size: int, grid: Grid = None) -> None:
        """
        Initialize a stonehenge state and set the current player based on
        p1_starts.

        Extends GameState.__init__
        """
        GameState.__init__(self, is_p1_turn)
        self.grid = Grid(size) if not grid else grid
        self.p1, self.p2, self.size = 0, 0, size

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.

        Overrides GameState.__str__
        """
        template = self.get_template()
        size_1 = """\
      {l1}   {l2}
     /   /
{ley1} - {A} - {B}
     \\ / \\
  {ley2} - {C}   {r1}
       \\
        {r2}"""
        size_2 = """\
        {l1}   {l2}
       /   /
  {ley1} - {A} - {B}   {l3}
     / \\ / \\ /
{ley2} - {C} - {D} - {E}
     \\ / \\ / \\
  {ley3} - {F} - {G}   {r1}
       \\   \\
        {r3}   {r2}"""
        size_3 = """\
          {l1}   {l2}
         /   /
    {ley1} - {A} - {B}   {l3}
       / \\ / \\ /
  {ley2} - {C} - {D} - {E}   {l4}
     / \\ / \\ / \\ /
{ley3} - {F} - {G} - {H} - {I}
     \\ / \\ / \\ / \\
  {ley4} - {J} - {K} - {L}   {r1}
       \\   \\   \\
        {r4}   {r3}   {r2}"""
        size_4 = """\
            {l1}   {l2}
           /   /
      {ley1} - {A} - {B}   {l3}
         / \\ / \\ /
    {ley2} - {C} - {D} - {E}   {l4}
       / \\ / \\ / \\ /
  {ley3} - {F} - {G} - {H} - {I}   {l5}
     / \\ / \\ / \\ / \\ /
{ley4} - {J} - {K} - {L} - {M} - {N}
     \\ / \\ / \\ / \\ / \\
  {ley5} - {O} - {P} - {Q} - {R}   {r1}
       \\   \\   \\   \\
        {r5}   {r4}   {r3}   {r2}"""
        size_5 = """\
              {l1}   {l2}
             /   /
        {ley1} - {A} - {B}   {l3}
           / \\ / \\ /
      {ley2} - {C} - {D} - {E}   {l4}
         / \\ / \\ / \\ /
    {ley3} - {F} - {G} - {H} - {I}   {l5}
       / \\ / \\ / \\ / \\ /
  {ley4} - {J} - {K} - {L} - {M} - {N}   {l6}
     / \\ / \\ / \\ / \\ / \\ /
{ley5} - {O} - {P} - {Q} - {R} - {S} - {T}
     \\ / \\ / \\ / \\ / \\ / \\
  {ley6} - {U} - {V} - {W} - {X} - {Y}   {r1}
       \\   \\   \\   \\   \\
        {r6}   {r5}   {r4}   {r3}   {r2}"""
        size = {1: size_1, 2: size_2, 3: size_3, 4: size_4, 5: size_5}
        return size[self.size].format(**template)

    def get_template(self) -> dict:
        """
        Return a dictionary that templates the string representation of
        StonehengeState.
        """
        template = {}
        i = 0
        while i <= self.size:
            template['ley{}'.format(i + 1)] = self.grid.leylines[i].player
            i += 1
        i = 0
        while i <= self.size:
            template['l{}'.format(i + 1)] = self.grid.lefts[i].player
            i += 1
        i = 0
        while i <= self.size:
            template['r{}'.format(i + 1)] = self.grid.rights[i].player
            i += 1
        for cell in self.grid.cells:
            template[cell.letter] = str(cell)
        return template

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.

        Overrides GameState.get_possible_moves()
        """
        result = self.p1 >= (int(self.size) + 1) * 3 / 2 or self.p2 >= \
            (int(self.size) + 1) * 3 / 2
        return [] if result else [str(n) for n in self.grid.cells
                                  if n.player == 0]

    def make_move(self, move: Any) -> 'StonghengeState':
        """
        Return the StonehengeState that results from applying move to this
        StonehengeState.

        Overrides GameState.make_move()
        """
        new_state = StonehengeState(not self.p1_turn, self.size,
                                    self.grid.copy())
        new_state.grid.update_grid(self.get_current_player_name(), move)
        new_state.p1, new_state.p2 = new_state.grid.get_score(1),\
            new_state.grid.get_score(2)
        return new_state

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).

        Overrides GameState.__repr__
        """
        temp_1 = 'Current player: {}\n'.format(self.get_current_player_name())
        temp_2 = 'Cells: ' + ', '.join(['{}-{}'.format(n.letter, n.player) for
                                        n in self.grid.cells]) + '\n'
        return temp_1 + temp_2

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.

        Overrides GameState.rough_outcome()
        """
        if self.get_possible_moves() == []:
            return 1 if self.get_winner() == self.get_current_player_name() \
                else -1
        if any([self.finished(move) for move in self.get_possible_moves()]):
            return 1
        result = []
        for move in self.get_possible_moves():
            new_state = self.make_move(move)
            result.append(any([new_state.make_move(move) for move
                               in new_state.get_possible_moves()]))
        if all(result):
            return -1
        return 0

    def finished(self, move) -> bool:
        """
        Return True if the move applied will finish the game.
        """
        return self.make_move(move).p1 >= (int(self.size) + 1) * 3 / 2 or \
            self.make_move(move).p2 >= (int(self.size) + 1) * 3 / 2

    def get_winner(self) -> str:
        """
        Return a string of the player which is the winner of the game.
        """
        return 'p1' if self.p1 >= (int(self.size) + 1) * 3 / 2 else 'p2'


def gather_str(lst: 'list[Any]') -> 'list[str]':
    """
    Return a list of string based on lst.
    """
    if not isinstance(lst, list):
        return [lst] if isinstance(lst, str) else []
    return sum([gather_str(x) for x in lst], [])


def get_leyline(side: int) -> 'list[list]':
    """
    Return a ley-line state of list for the instance of stonehenge.
    """
    cell = [chr(65 + n) for n in range(26)]
    length, start, result = 2, 0, []
    while length <= side + 1:
        result.append(cell[start:start + length])
        start += length
        length += 1
    result.append(cell[start:start + side])
    return result


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
