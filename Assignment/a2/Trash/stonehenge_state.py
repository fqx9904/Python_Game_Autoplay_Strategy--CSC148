"""
A stonehenge_state module
"""
from typing import Any
from game_state import GameState
from grid import Grid


class StonehengeState(GameState):
    """
    The state of stonehenge game at a certain point of time.

    is_p1_turn - whether it's the turn for p1
    size - the side-length of the stonehenge
    grid - a grid for stonehenge game
    """
    is_p1_turn: bool
    size: int
    grid: Grid

    check_for_str = '      @   @\n     /   /\n@ - A - B\n  ' \
                    '   \\ / \\\n  @ - C   @\n       \\\n        @'

    def __init__(self, is_p1_turn: bool, size: int, grid: Grid = None) -> None:
        """
        Initialize a stonehenge state and set the current player based on
        p1_starts.

        Extends GameState.__init__

        >>> state = StonehengeState(True, 1)
        >>> print([str(cell) for cell in state.grid.cells])
        ['A', 'B', 'C']
        >>> state.p1
        0
        """
        GameState.__init__(self, is_p1_turn)
        self.grid = Grid(size) if not grid else grid
        self.p1, self.p2, self.size = 0, 0, size

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.

        Overrides GameState.__str__

        >>> state = StonehengeState(True, 1)
        >>> str(state) == StonehengeState.check_for_str
        True
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

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).

        Overrides GameState.__repr__

        >>> state = StonehengeState(True, 1)
        >>> print(repr(state))
        Current player: p1
        Cells: A-0, B-0, C-0
        p1_score: 0, p2_score: 0
        """
        temp_1 = 'Current player: {}\n'.format(self.get_current_player_name())
        temp_2 = 'Cells: ' + ', '.join(['{}-{}'.format(n.letter, n.player) for
                                        n in self.grid.cells]) + '\n'
        temp_3 = 'p1_score: {}, p2_score: {}'.format(self.p1, self.p2)
        return temp_1 + temp_2 + temp_3

    def __eq__(self, other: Any) -> bool:
        """
        Return whether self and other is equivalent.

        >>> a = StonehengeState(True, 1)
        >>> b = StonehengeState(True, 1)
        >>> a == b
        True
        """
        return type(self) == type(other) and repr(self) == repr(other)

    def get_template(self) -> dict:
        """
        Return a dictionary that templates the string representation of
        StonehengeState.

        >>> state = StonehengeState(True, 1)
        >>> state.get_template() == {'ley1': '@', 'l1': '@', 'r1': '@', \
        'ley2': '@', 'l2': '@', 'r2': '@', 'A': 'A', 'B': 'B', 'C': 'C'}
        True
        """
        template = {}
        i = 0
        while i <= self.size:
            template['ley{}'.format(i + 1)] = self.grid.leylines[i].player
            template['l{}'.format(i + 1)] = self.grid.lefts[i].player
            template['r{}'.format(i + 1)] = self.grid.rights[i].player
            i += 1
        for cell in self.grid.cells:
            template[cell.letter] = str(cell)
        return template

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.

        Overrides GameState.get_possible_moves()

        >>> state = StonehengeState(True, 1)
        >>> state.get_possible_moves()
        ['A', 'B', 'C']
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

        >>> state = StonehengeState(True, 1)
        >>> new_state = state.make_move('A')
        >>> new_state.p1_turn
        False
        >>> id(new_state) == id(state)
        False
        """
        new_state = StonehengeState(not self.p1_turn, self.size,
                                    self.grid.copy())
        new_state.grid.update_grid(self.get_current_player_name(), move)
        new_state.p1, new_state.p2 = new_state.grid.get_score(1),\
            new_state.grid.get_score(2)
        return new_state

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.

        Overrides GameState.rough_outcome()

        >>> state = StonehengeState(True, 1)
        >>> state.rough_outcome()
        1
        >>> new_state = state.make_move('A')
        >>> new_state.rough_outcome()
        -1
        >>> state = StonehengeState(True, 3)
        >>> state.rough_outcome()
        0
        """
        if self.get_possible_moves() == []:
            return 1 if self.get_winner() == self.get_current_player_name() \
                else -1
        if any([self.finished(move) for move in self.get_possible_moves()]):
            return 1
        result = []
        for move in self.get_possible_moves():
            new_state = self.make_move(move)
            result.append(any([new_state.finished(move) for move
                               in new_state.get_possible_moves()]))
        return -1 if all(result) else 0

    def finished(self, move) -> bool:
        """
        Return True if the move applied will finish the game.

        >>> StonehengeState(True, 1).finished('A')
        True
        >>> StonehengeState(True, 2).finished('A')
        False
        """
        return self.make_move(move).p1 >= (int(self.size) + 1) * 3 / 2 or \
            self.make_move(move).p2 >= (int(self.size) + 1) * 3 / 2

    def get_winner(self) -> str:
        """
        Return a string of the player which is the winner of the game.

        >>> StonehengeState(True, 1).make_move('A').get_winner()
        'p1'
        """
        return 'p1' if self.p1 >= (int(self.size) + 1) * 3 / 2 else 'p2'


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

    import doctest
    doctest.testmod()
