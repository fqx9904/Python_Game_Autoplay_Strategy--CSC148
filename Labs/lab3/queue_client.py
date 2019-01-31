from csc148_queue import Queue


def list_queue(self, lst: list) -> None:
    """Docstring.
    """
    for item in lst:
        self.add(item)
    while not self.is_empty():
        first = self.remove()
        if isinstance(first, list):
            for element in first:
                self.add(element)
        else:
            print(first)


if __name__ == '__main__':

    list_queue(Queue(), [1, [3, [5, 7], 9], 11])
    #list_queue(Queue(), [1, [3, 5], 7])
