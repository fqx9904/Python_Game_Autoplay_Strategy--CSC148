from typing import Union


class LinkedListNode:
    """
    Node to be used in linked list

    next_ - successor to this LinkedListNode
    value - data this LinkedListNode represents
    """
    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
                 next_: Union["LinkedListNode", None] = None) -> None:
        """
        Create LinkedListNode self with data value and successor next_.
        """
        self.value, self.next_ = value, next_

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this LinkedListNode.

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        s = "{} ->".format(self.value)
        current_node = self.next_
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        return s + "|"


class LinkedList:
    """
    Collection of LinkedListNodes

    front - first node of this LinkedList
    size - number of nodes in this LinkedList, >= 0
    """
    front: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Create an empty linked list.
        """
        self.front, self.size = None, 0

    def __setitem__(self, index: int, value: object) -> None:
        """
        Set the value of list at position index to value. Raise IndexError
        if index >= self.size or index < -self.size

        >>> lnk = LinkedList()
        >>> lnk.front = LinkedListNode(3, None) # Insert in reverse
        >>> lnk.front = LinkedListNode(2, lnk.front)
        >>> lnk.front = LinkedListNode(1, lnk.front) # lnk.front has value 1 now
        >>> lnk.size = 3
        >>> print(lnk.front) # note that lnk.front contains 1
        1 -> 2 -> 3 ->|
        >>> lnk[2] = 5
        >>> print(lnk.front)
        1 -> 2 -> 5 ->|
        >>> lnk[-1] = 6 # one from the end
        >>> print(lnk.front)
        1 -> 2 -> 6 ->|
        """
        # TODO: implement the body of this method.
        # You need not touch any other code than the body of this method
        # You need not add comments or docstrings.
        # You need only add the preconditions that we specify.
        if index >= self.size or index < -self.size:
            raise IndexError('Oh No!')
        temp = self.front
        for _ in range(index if index >= 0 else self.size + index):
            temp = temp.next_
        temp.value = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
