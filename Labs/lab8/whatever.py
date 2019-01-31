"""
module
"""


class BTNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data, self.left, self.right = data, left, right


def TPBT(root) -> tuple:
    def height(root) -> int:
        if not root:
            return 0
        return 1 + max(height(root.right), height(root.left))

    def is_PT(root) -> bool:
        if not root or (not root.left and not root.right):
            return True
        return is_PT(root.left) and is_PT(root.right) and height(root.left) \
            == height(root.right)

    def tallest(root) -> int:
        if is_PT(root):
            return height(root)
        return max(tallest(root.left), tallest(root.right))

    return (tallest(root), tallest(root) == height(root))


class Tree:
    def __init__(self, value=None, children=[]) -> None:
        self.value, self.children = value, children


def unique_paths(t) -> bool:
    r = set()

    def helper(t, record) -> bool:
        if not t.children:
            return True
        record.add(t)
        for c in t.children:
            if c in record:
                return False
            record.add(c)
            if not helper(c, record):
                return False
        return True
    return helper(t, r)


def width(lst: list, d: int) -> int:
    def helper(lst, d) -> dict:
        result = {d: len(lst)}
        if d == 0:
            return result
        for i in lst:
            if isinstance(i, list):
                temp = helper(i, d - 1)
                for k in temp:
                    if k not in result:
                        result[k] = 0
                    result[k] += temp[k]
        return result

    result = helper(lst, d)
    return max(result.values())


def width_new(lst, d) -> int:
    def count_by_depth(lst, d) -> list:
        if d == 0:
            return [1]
        result = [1]
        for item in lst:
            temp = count_by_depth(item, d - 1) if isinstance(item, list) \
                else [1]
            for i in range(len(temp)):
                if len(result) - 1 < i + 1:
                    result.append(temp[i])
                else:
                    result[i + 1] += temp[i]
        return result
    return max(count_by_depth(lst, d))


def count_by_level(t: Tree) -> list:
    result = [1]
    after = []
    for c in t.children:
        temp = count_by_level(c)
        for i in range(len(temp)):
            if len(after) < i + 1:
                after.append(temp[i])
            else:
                after[i] += temp[i]
    return result + after


def extend_third_level(t: Tree) -> None:
    def helper(t, d) -> None:
        if d % 3 == 0:
            t.children = [Tree(t.value, t.children[:])]
            for c in t.children[0].children:
                helper(c, d + 1)
        else:
            for c in t.children:
                helper(c, d + 1)
    helper(t, 1)


def prune(t, predicate) -> 'Union[Tree, None]':
    if not predicate(t.value):
        return None
    t.children = [prune(c, predicate) for c in t.children[:]
                  if prune(c, predicate)]
    return t


def foo(k):
    k.append(k.append(1))


def bar(list_):
    new = []
    for item in list_:
        new.append(item + 100)
    list_, new = new, list_


if __name__ == '__main__':
    # t1 = Tree(1)
    # t2 = Tree(2)
    # t3 = Tree(3, [t1, t2])
    # t4 = Tree(4, [t3, t1])
    # print(unique_paths(t4))
    # print(unique_paths(t1))
    # print(count_by_level(t3))
    # t5 = Tree(5, [t3])
    # print(count_by_level(t5))
    # extend_third_level(t5)
    # print(count_by_level(t5))

    # lst = [[0, 1], 2, [3, [[], 4]]]
    # print(width_new(lst, 4))
    # lst2 = [0, 1]
    # print(width_new(lst2, 1))

    # t1 = Tree(6, [Tree(8), Tree(9)])
    # t2 = Tree(4, [Tree(11), Tree(12)])
    # print(prune(t1, f) == t1)

    q = [0]
    bar(q)
    print(q)
