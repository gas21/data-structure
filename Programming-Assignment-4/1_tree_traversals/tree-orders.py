# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)   # new thread will get stack of such size


result1 = []
result2 = []
result3 = []


class Tree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def read():
    n = int(sys.stdin.readline())
    key = [0 for _ in range(n)]
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    for i in range(n):
        [a, b, c] = map(int, sys.stdin.readline().split())
        key[i] = a
        left[i] = b
        right[i] = c
    return key, left, right


def build_tree(tree, index):
    k, l, r = tree[index]
    if l == -1 and r == -1:
        return Tree(k, -1, -1)
    elif l == -1 and r != -1:
        return Tree(k, -1, build_tree(tree, r))
    elif l != -1 and r == -1:
        return Tree(k, build_tree(tree, l), -1)
    else:
        return Tree(k, build_tree(tree, l), build_tree(tree, r))


def in_order(tree):
    global result1
    if not isinstance(tree, Tree):
        return
    in_order(tree.left)
    result1.append(tree.key)
    in_order(tree.right)


def pre_order(tree):
    global result2
    if not isinstance(tree, Tree):
        return
    result2.append(tree.key)
    pre_order(tree.left)
    pre_order(tree.right)


def post_order(tree):
    global result3
    if not isinstance(tree, Tree):
        return
    post_order(tree.left)
    post_order(tree.right)
    result3.append(tree.key)


def main():
    key, left, right = read()
    trees = [(i, j, k) for i, j, k in zip(key, left, right)]
    tree = build_tree(trees, 0)
    in_order(tree)
    pre_order(tree)
    post_order(tree)
    print(" ".join(str(x) for x in result1))
    print(" ".join(str(x) for x in result2))
    print(" ".join(str(x) for x in result3))


threading.Thread(target=main).start()
