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

    def load_list(self, items):
        """ Load items to the end of self.

        >>> lnk = LinkedList()
        >>> lnk.load_list([1,2,3,4])
        >>> print(lnk)
        1 -> 2 -> 3 -> 4 ->|
        """

        for item in items:
            node = LinkedListNode(item)
            if self.size == 0:
                self.front, self.back = node, node
            else:
                self.back.next_ = node
                self.back = node
            self.size += 1

    def add_one(self) -> None:
        """ Add one to each item in the linkedlist
        
        >>> lnk = LinkedList()
        >>> lnk.load_list([0, 1, 2])
        >>> lnk.add_one()
        >>> print(lnk)
        1 -> 2 -> 3 ->|
        """
        temp = self.front
        for _ in range(self.size):
            temp.value += 1
            temp = temp.next_
        

    def insert(self, index: int, item: object) -> None:
        """ Insert the item before the index such as
        list's insert method. Assume the index is valid
        
        >>> lnk = LinkedList()
        >>> lnk.load_list([1, 2, 3])
        >>> lnk.insert(0, 0)
        >>> lnk.insert(4, 4)
        >>> print(lnk)
        0 -> 1 -> 2 -> 3 -> 4 ->|
        """
        if index == 0:
            self.front = LinkedListNode(item, self.front)
            if not self.back:
                self.back = self.front
        else:
            temp = self.front
            for _ in range(index - 1):
                temp = temp.next_
            temp.next_ = LinkedListNode(item, temp.next_)

            if self.back.next_:
                self.back = self.back.next_

        self.size += 1




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
        if index == 0:
            result = self.front.value
            self.front = self.front.next_
            self.size -= 1
            if not self.front:
                self.back = None

        else:
            temp = self.front
            for _ in range(index - 1):
                temp = temp.next_

            result = temp.next_.value
            temp.next_ = temp.next_.next_
            self.size -= 1

            if not temp.next_:
                self.back = temp


        return result



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
        # Only if the linkedlist is not empty
        if self.size > 0:
            # Handle head
            if self.front.value % 2 == 1:
                self.front = self.front.next_
                self.size -= 1
                # Update back if needed
                if not self.front:
                    self.back = None
            # In the middle or at the end.
            else:
                temp = self.front
                # Try to find target
                while temp.next_ and temp.next_.value % 2 == 0:
                    temp = temp.next_
                # If found
                if temp.next_:
                    temp.next_ = temp.next_.next_
                    self.size -= 1
                    # Update Back if needed
                    if not temp.next_:
                        self.back = temp

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
        if self.size > 0:

            while self.front and self.front.value % 2 == 1:
                self.front = self.front.next_
                self.size -= 1

            if not self.front:
                self.back = None

            else:
                temp = self.front
                while temp.next_:
                    if temp.next_.value % 2 == 1:
                        temp.next_ = temp.next_.next_
                        self.size -= 1
                    else:
                        temp = temp.next_
                self.back = temp





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
        if self.size > 0:
            temp = self.front
            while temp.next_:
                if temp.next_.value == temp.value:
                    temp.next_ = temp.next_.next_
                    self.size -= 1
                else:
                    temp = temp.next_
            self.back = temp



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
        temp = self.front
        while temp and temp.value % 2 == 0:
            temp = temp.next_
        if temp:
            temp.next_ = LinkedListNode(temp.value, temp.next_)
            self.size += 1
            if not temp.next_.next_:
                self.back = temp.next_.next_


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
        temp = self.front
        while temp:
            if temp.value % 2 == 1:
                temp.next_ = LinkedListNode(temp.value, temp.next_)
                self.size += 1
                temp= temp.next_

            if not temp.next_:
                self.back = temp

            temp = temp.next_

        

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
        if self.size >= 2:
            temp = self.front
            for _ in range(self.size - 2):
                temp = temp.next_

            # New front
            temp.next_.next_ = self.front
            self.front = temp.next_

            # New back
            self.back = temp
            self.back.next_ = None


    def reverse(self) -> None:
        """ Reverse the entire linkedlist.

        >>> a = LinkedList()
        >>> a.load_list([1, 2, 3])
        >>> a.right_shift()
        >>> print(a)
        3 -> 2 -> 1 ->|
        """
        if self.front and self.front.next_:
            ptr = self.front
            temp = ptr.next_
            while temp:
                ori_next_ = temp.next_
                temp.next_ = ptr
                ptr = temp
                temp = ori_next_
            # update front 
            self.front.next_ = None
            self.front, self.back = self.back, self.front
        



if __name__ == '__main__':
    import doctest
    doctest.testmod()