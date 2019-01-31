"""
stack client code
"""
from stack import Stack


def list_stack(self, lst: list) -> None:
    """Docstring.
    """
    for element in lst:
        self.add(element)
    while not self.is_empty():
        top = self.remove()
        if isinstance(top, list):
            for element in top:
                self.add(element)
        else:
            print(top)


if __name__ == '__main__':
    new_stack = Stack()
    new_string = input('Type a string:')

    while new_string.lower() != 'end':
        new_stack.add(new_string)
        new_string = input('Type a string:')

    while not new_stack.is_empty():
        print(new_stack.remove())

    list_stack(Stack(), [1, [3, [5, 7], 9], 11])

