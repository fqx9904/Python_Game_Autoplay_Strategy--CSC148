from stack import Stack


def get_largest(stack: Stack) -> int:
    """Return the largest from the stack.

    Precondition: stack contains only int

    >>> stack = Stack()
    >>> stack.add(1)
    >>> stack.add(2)
    >>> get_largest(stack)
    2
    """
    pass


def double_items(stack: Stack) -> None:
    """Double all items in the given stack

    Precondition: stack contains only numbers

    >>> stack = Stack()
    >>> stack.add(1)
    >>> stack.add(2)
    >>> double_items(stack)
    >>> stack.remove()
    4
    >>> stack.remove()
    2
    """
    pass


def copy_stack(stack: Stack) -> Stack:
    """Remove a new Stack that is identical to the given stack

    >>> stack = Stack()
    >>> stack.add(1)
    >>> stack.add(2)
    >>> stack2 = copy_stack(stack)
    >>> stack.remove() == stack2.remove()
    True
    >>> stack.remove() == stack2.remove()
    True
    >>> stack.is_empty() and stack2.is_empty()
    True
    """
    pass


def reverse(stack: Stack) -> None:
    """Reverse the order of <stack>.

    @param Stack stack:
    @rtype: None

    >>> stack = Stack()
    >>> stack.add(1)
    >>> stack.add(2)
    >>> reverse(stack)
    >>> stack.remove()
    1
    >>> stack.remove()
    2
    """
    pass


"""
Complete the implementation of push in the class DividingStack, a subclass of Stack,
Notice that you may use add, remove and is_empty, the public operation of Stack, but
you may not assume anything about Stack's implementation. You may find it useful to
know that if n1 and n2 are integers, then n1 % n2 == 0 if and only if n2 divides n1
evenly.
"""


class DividingStack(Stack):
    """ A stack of integers that divide predecessors """

    def add(self, n: int) -> None:
        """Add n on top of self if it evenly divides its predecessor or self is empty.
        Otherwise, raise a ValueError and leave self as it was before.

        Precondition: Possibly empty self contains only Integers.

        >>> s = DividingStack()
        >>> s.push(12)
        >>> s.push(4)
        >>> # now s.push(3) should raise Exception.
        """
        pass
