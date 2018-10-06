"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def add_score(state: Any, score: int) -> Any:
    """
    Add the score attribute to the state.
    """
    state.score = score
    return state


# TODO: Implement a recursive version of the minimax strategy.
def recursive_minimax(game: Any) -> Any:
    """
    Return the best move for the current player by the minimax concept and
    calculating the result recursively.
    """
    state = add_score(game.current_state, -2)
    player = state.get_current_player_name()
    moves = state.get_possible_moves()
    choices = [add_score(state.make_move(move), -2) for move in moves]
    scores = []

    for choice in choices:
        new_game = game
        new_game.current_state = choices[choices.index(choice)]

        if new_game.is_winner(player):
            state.score = 1
            game.current_state = state
            return moves[choices.index(choice)]
        elif new_game.is_over(choice):
            choices[choices.index(choice)].score = -1 \
                if new_game.is_winner('p2' if 'p1' == player else 'p1') else 0
        else:
            recursive_minimax(new_game)
            choices[choices.index(choice)].score = -1 * \
                new_game.current_state.score
        scores.append(choice.score)

    game.current_state = state
    state.score = max(scores)
    for choice in choices:
        if choice.score == max(scores):
            return moves[choices.index(choice)]
    return 'Whatever Something.'


class GameNode:
    """
    A GameNode for iterative minimax.

    current_state - the current game state.
    score - the best score that the player can get.
    id - the GameNode id for tracking.
    """
    current_state: Any
    id_num: int
    move: Any
    children: 'list[int]'
    score: int

    def __init__(self, current_state: Any, id_num: int, move: Any = None,
                 children_score: tuple = None) -> None:
        """
        Initialize a GameNode with current state, score and id.
        """
        self.current_state, self.id_num, self.move = current_state, id_num, move
        self.children = children_score[0] if children_score else children_score
        self.score = children_score[1] if children_score else children_score


class Stack:
    """
    A Stack data structure.

    _stack - a stack list.
    """
    _stack: list

    def __init__(self, stack: list = None) -> None:
        """
        Initialize a Stack.
        """
        self._stack = [] if not stack else stack

    def append(self, other: Any) -> None:
        """
        Add other to the stack.
        """
        self._stack.append(other)

    def remove(self) -> Any:
        """
        Return and remove the top item from the stack.
        """
        return self._stack.pop(-1)

    def is_empty(self) -> bool:
        """
        Return whether the stack is empty.
        """
        return self._stack == []


# TODO: Implement an iterative version of the minimax strategy.
def iterative_minimax(game: Any) -> Any:
    """
    Return the best move for the game using the minimax strategy iteratively.
    """
    stack = Stack()
    id_num = 0
    stack.append(GameNode(game.current_state, id_num))
    result = {}
    while not stack.is_empty():
        node = stack.remove()
        game.current_state = node.current_state
        player = node.current_state.get_current_player_name()
        if game.is_over(node.current_state):
            node.score = 1 if game.is_winner(player) else \
                (-1 if game.is_winner('p2' if 'p1' == player else 'p1') else 0)
            result[node.id_num] = node
        elif not node.children:
            stack.append(node)
            node.children = []
            for m in node.current_state.get_possible_moves():
                id_num += 1
                sub_node = GameNode(node.current_state.make_move(m), id_num, m)
                node.children.append(id_num)
                stack.append(sub_node)
        else:
            max_score = max([-1 * result[n].score for n in node.children])
            node.score = max_score
            result[node.id_num] = node
    for num in result[0].children:
        if result[num].score == -1 * result[0].score:
            return result[num].move
    return 'Turin Bless Me !'


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
