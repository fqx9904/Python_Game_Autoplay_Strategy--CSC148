""" practice on linked lists
"""


class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
    @param LinkedListNode next_: successor to this LinkedListNode
    @param object value: data this LinkedListNode represents
    """
    def __init__(self, value, next_=None):
        """
        Create LinkedListNode self with data value and successor next_.

        @param LinkedListNode self: this LinkedListNode
        @param object value: data of this linked list node
        @param LinkedListNode|None next_: successor to this LinkedListNode.
        @rtype: None
        """
        self.value, self.next_ = value, next_

    def __str__(self):
        """
        Return a user-friendly representation of this LinkedListNode.

        @param LinkedListNode self: this LinkedListNode
        @rtype: str

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        # start with a string s to represent current node.
        s = "{} ->".format(self.value)
        # create a reference to "walk" along the list
        current_node = self.next_
        # for each subsequent node in the list, build s
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s


class LinkedList:
    """
    Collection of LinkedListNodes

    === Attributes ==
    @param: LinkedListNode front: first node of this LinkedList
    @param LinkedListNode back: last node of this LinkedList
    @param int size: number of nodes in this LinkedList
                        a non-negative integer
    """
    def __init__(self):
        """
        Create an empty linked list.

        @param LinkedList self: this LinkedList
        @rtype: None
        """
        self.front, self.back, self.size = None, None, 0

    def __str__(self):
        """
        Return a human-friendly string representation of
        LinkedList self.

        @param LinkedList self: this LinkedList

        >>> lnk = LinkedList()
        >>> print(lnk)
        I'm so empty... experiencing existential angst!!!
        """
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "I'm so empty... experiencing existential angst!!!"
        else:
            # use front.__str__() if this list isn't empty
            return str(self.front)

    def load_list(self, items) -> None:
        """ Load items to the end of self.

        >>> lnk = LinkedList()
        >>> lnk.load_list([1,2,3,4])
        >>> print(lnk)
        1 -> 2 -> 3 -> 4 ->|
        """
        pass

    def add_one(self) -> None:
        """ Add one to each item in the linkedlist
        
        >>> lnk = LinkedList()
        >>> lnk.load_list([0, 1, 2])
        >>> lnk.add_one()
        >>> print(lnk)
        1 -> 2 -> 3 ->|
        """
        pass

    def insert(self, index: int, item: object) -> None:
        """ Insert the item before the index such as
        list's insert method. Assume the index is valid
        
        >>> lnk = LinkedList()
        >>> lnk.load_list([1, 2, 3])
        >>> lnk.insert(0, 1)
        >>> lnk.insert(4, 4)
        >>> print(lnk)
        0 -> 1 -> 2 -> 3 -> 4 ->|
        """
        pass

    def pop(self, index: int) -> object:
        """ pop the item aat the index such as
        list's pop method. Assume the index is valid
        
        >>> lnk = LinkedList()
        >>> lnk.load_list([0, 1, 2])
        >>> lnk.pop(0)
        0
        >>> print(lnk)
        1 -> 2 ->|
        """
        pass


    def delete_first_odd(self) -> None:
        """ delete all nodes that contains odd value.

        Delete the first odd node in self.

        @type self: Linkedlist
        @rtype: None

        >>> a = LinkedList()
        >>> a.load_list([1, 2, 3, 4, 5])
        >>> a.delete_first_odd()
        >>> print(a)
        2 -> 3 -> 4 -> 5 ->|
        >>> a.delete_first_odd()
        >>> print(a)
        2 -> 4 -> 5 ->|
        """
        pass

    def delete_all_odd(self) -> None:
        """ delete all nodes that pass the passr.

        Delete All Odd from the self.

        @type self: Linkedlist
        @rtype: None

        >>> a = LinkedList()
        >>> a.load_list([1, 2, 3, 4, 5])
        >>> a.delete_all_odd()
        >>> print(a)
        2 -> 4 ->|
        """
        pass



    def delete_consecutive_duplicate(self) -> None:
        """ Delete all consecutive duplicates in self.

        @type self: Linkedlist
        @rtype: None

        >>> a = LinkedList()
        >>> a.load_list([1, 2, 2, 2, 5])
        >>> a.delete_consecutive_duplicate()
        >>> print(a)
        1 -> 2 -> 5 ->|
        """
        pass



    def copy_first_odd(self) -> None:
        """ Copy first nodes by add the same node after it.

        @type self: Linkedlist
        @rtype: None

        >>> a = LinkedList()
        >>> a.load_list([1, 2, 3])
        >>> a.double_first_odd()
        >>> print(a)
        1 -> 1 -> 2 -> 3 ->|
        """
        pass


    def copy_all_odd(self) -> None:
        """ Double all nodes by add the same node after them.

        @type self: Linkedlist
        @rtype: None

        >>> a = LinkedList()
        >>> a.load_list([1, 2, 3])
        >>> a.double_all_odd()
        >>> print(a)
        1 -> 1 -> 2 -> 3 -> 3 ->|
        """
        pass

        

    def right_shift(self) -> None:
        """  Right shift the linkedlist by 1, so the last node becomes the first.
        Nothing would happend when the size of self is less than 2.

        @type self: LinkedList
        @rtype: None

        >>> a = LinkedList()
        >>> a.load_list([1, 2, 3])
        >>> a.right_shift()
        >>> print(a)
        3 -> 1 -> 2 ->|
        """
        pass


    def reverse(self) -> None:
        """ Reverse the entire linkedlist.

        >>> a = LinkedList()
        >>> a.load_list([1, 2, 3])
        >>> a.right_shift()
        >>> print(a)
        3 -> 2 -> 1 ->|
        """
        pass



if __name__ == '__main__':
    import doctest
    doctest.testmod()
