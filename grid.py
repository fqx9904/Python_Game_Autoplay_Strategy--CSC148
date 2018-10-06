"""
A grid module
"""
from typing import Any


class Cell:
    """
    A cell for the stonehenge game.

    letter - a letter represents the cell
    player - the player claims the cell, 1 for player_1 and 2 for player_2
    """
    letter: str
    player: int

    def __init__(self, letter: str, player: int = 0) -> None:
        """
        Initialize a cell with letter and player.

        >>> cell = Cell('A')
        >>> cell.player
        0
        >>> cell.letter
        'A'
        """
        self.letter, self.player = letter, player

    def __str__(self) -> str:
        """
        Return the string representation of a cell.

        >>> cell = Cell('A')
        >>> str(cell)
        'A'
        """
        return '{}'.format(self.letter if self.player == 0 else self.player)

    def update_cell(self, player: str, letter: str) -> 'Cell':
        """
        Update the cell claimed by players.

        >>> cell = Cell('A')
        >>> cell = cell.update_cell('p2', 'A')
        >>> cell.player
        2
        """
        if self.player == 0 and self.letter == letter:
            self.player = 1 if player == 'p1' else 2
        return self

    def copy(self) -> 'Cell':
        """
        Return a new instance of Cell with the same attributes.

        >>> a = Cell('A')
        >>> b = a.copy()
        >>> id(a) == id(b)
        False
        >>> b.letter
        'A'
        """
        new = Cell(self.letter)
        new.player = self.player
        return new


class Line:
    """
    A line for the stonehenge game.

    cells - the cells in that line
    player - the player claims the line, 1 for player_1 and 2 for player_2
    """
    cells: 'list[Cell]'
    player: int

    def __init__(self, cells: 'list[Cell]', player: Any = '@') -> None:
        """
        Initialize a line with cells and player.

        >>> line = Line([Cell('A')])
        >>> line.player
        '@'
        >>> print([str(cell) for cell in line.cells])
        ['A']
        """
        self.cells, self.player = cells, player
        self.player_1, self.player_2, self.total = 0, 0, len(self.cells)

    def copy(self) -> 'Line':
        """
        Return a new instance of Cell with the same attributes.

        >>> a = Line([Cell('A')])
        >>> b = a.copy()
        >>> id(a) == id(b)
        False
        >>> print([str(cell) for cell in b.cells])
        ['A']
        """
        new = Line([cell.copy() for cell in self.cells], self.player)
        new.player_1, new.player_2 = self.player_1, self.player_2
        return new

    def update_line(self, player: str, letter: str) -> None:
        """
        Update the line claimed by players.

        >>> line = Line([Cell('A'), Cell('B')])
        >>> line.update_line('p1', 'B')
        >>> line.player
        1
        >>> print([str(cell) for cell in line.cells])
        ['A', '1']
        """
        if self.player == '@':
            i = 0
            while i < len(self.cells):
                self.cells[i] = self.cells[i].update_cell(player, letter)
                i += 1
            self.check_score()
            if self.player_1 >= self.total / 2:
                self.player = 1
            elif self.player_2 >= self.total / 2:
                self.player = 2

    def check_score(self) -> None:
        """
        Update the score fo each player on the Line.

        >>> line = Line([Cell('A'), Cell('B')])
        >>> line.cells[1] = line.cells[1].update_cell('p1', 'B')
        >>> line.check_score()
        >>> line.player_1
        1
        >>> line.player_2
        0
        """
        self.player_1, self.player_2 = 0, 0
        for cell in self.cells:
            if cell.player == 1:
                self.player_1 += 1
            elif cell.player == 2:
                self.player_2 += 1


class Grid:
    """
    A grid for the game stonehenge.

    size - the size of the grid
    leyline - the leylines of the grid
    left - the left diagonals of the grid
    right - the right diagonals of the grid
    """
    cells: 'list[Cell]'
    size: int
    leylines: 'list[Line]'
    lefts: 'list[Line]'
    rights: 'list[Line]'

    def __init__(self, size: int, cells: 'list[Cell]' = None,
                 lines: tuple = None) -> None:
        """
        Initialize a grid for the game stonehenge.

        >>> grid = Grid(2)
        >>> len(grid.cells)
        7
        >>> print([str(cell) for cell in grid.leylines[0].cells])
        ['A', 'B']
        """
        self.size, self.cells = size, [Cell(chr(65 + n)) for n in
                                       range(int(((3 + size) * size / 2) +
                                                 size))] if not cells else cells
        if not lines:
            self.leylines = []
            interval = 2
            start = 0
            while interval <= size + 1:
                self.leylines.append(Line([self.cells[n] for n
                                           in range(start, start + interval)]))
                start, interval = start + interval, interval + 1
            self.leylines.append(Line([self.cells[n]
                                       for n in range(start, start + size)]))
            self.lefts = get_left(self.cells, size)
            self.rights = get_right(self.cells, size)
        else:
            self.leylines, self.rights, self.lefts = lines[0], lines[1], \
                                                     lines[2]

    def copy(self) -> 'Grid':
        """
        Return a same instance of Grid with different id.

        >>> a = Grid(2)
        >>> b = a.copy()
        >>> id(a) == id(b)
        False
        >>> [str(cell) for cell in a.cells] == [str(cell) for cell in b.cells]
        True
        """
        return Grid(self.size, [cell.copy() for cell in self.cells],
                    ([line.copy() for line in self.leylines],
                     [line.copy() for line in self.rights],
                     [line.copy() for line in self.lefts]))

    def update_grid(self, player: str, letter: str) -> None:
        """
        Update the Grid of player's claim. Only for Test purpose

        >>> grid = Grid(1)
        >>> grid.update_grid('p1', 'A')
        >>> print([str(i) for i in grid.cells])
        ['1', 'B', 'C']
        """
        self.cells = [cell.update_cell(player, letter) for cell in self.cells]
        i = 0
        while i <= self.size:
            self.leylines[i].update_line(player, letter)
            self.rights[i].update_line(player, letter)
            self.lefts[i].update_line(player, letter)
            i += 1

    def get_score(self, player: int) -> int:
        """
        Return the score for the player.

        >>> grid = Grid(1)
        >>> grid.update_grid('p1', 'A')
        >>> grid.get_score(1)
        3
        """
        score = 0
        i = 0
        while i < len(self.leylines):
            score += 1 if self.leylines[i].player == player else 0
            score += 1 if self.rights[i].player == player else 0
            score += 1 if self.lefts[i].player == player else 0
            i += 1
        return score


def get_left(lst: 'list[Cell]', size: int) -> 'list[Line]':
    """
    Return a list of Line which is the left diagonals based the stonehenge.

    >>> lefts = get_left([Cell(chr(65 + n)) for n in range(3)], 1)
    >>> len(lefts) == 2
    True
    >>> print([str(cell) for cell in lefts[1].cells])
    ['B', 'C']
    """
    form = {1: [[0], [1, 2]],
            2: [[0, 2], [1, 3, 5], [4, 6]],
            3: [[0, 2, 5], [1, 3, 6, 9], [4, 7, 10], [8, 11]],
            4: [[0, 2, 5, 9], [1, 3, 6, 10, 14], [4, 7, 11, 15], [8, 12, 16],
                [13, 17]],
            5: [[0, 2, 5, 9, 14], [1, 3, 6, 10, 15, 20], [4, 7, 11, 16, 21],
                [8, 12, 17, 22], [13, 18, 23], [19, 24]]}
    result = []
    for line in form[size]:
        result.append(Line([lst[n] for n in line]))
    return result


def get_right(lst: 'list[Cell]', size: int) -> 'list[Line]':
    """
    Return a list of Line which is the right diagonals based the stonehenge.

    >>> rights = get_right([Cell(chr(65 + n)) for n in range(3)], 1)
    >>> len(rights) == 2
    True
    >>> print([str(cell) for cell in rights[1].cells])
    ['A', 'C']
    """
    form = {1: [[1], [0, 2]],
            2: [[1, 4], [0, 3, 6], [2, 5]],
            3: [[1, 4, 8], [0, 3, 7, 11], [2, 6, 10], [5, 9]],
            4: [[1, 4, 8, 13], [0, 3, 7, 12, 17], [2, 6, 11, 16], [5, 10, 15],
                [9, 14]],
            5: [[1, 4, 8, 13, 19], [0, 3, 7, 12, 18, 24], [2, 6, 11, 17, 23],
                [5, 10, 16, 22], [9, 15, 21], [14, 20]]}
    result = []
    for line in form[size]:
        result.append(Line([lst[n] for n in line]))
    return result


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

    from doctest import testmod
    testmod()
