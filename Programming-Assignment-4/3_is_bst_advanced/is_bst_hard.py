#!/usr/bin/python3

import sys
import threading
import math

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

result1 = []


class Tree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


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


def is_binary_search_tree(tree, index, mini, maxi):
        # An empty tree is BST
        if index == -1:
            return True

        key, left, right = tree[index]

        if key < mini or key >= maxi:
            return False

        # Otherwise check the subtrees recursively
        # tightening the min or max constraint
        return is_binary_search_tree(tree, left, mini, key) and \
               is_binary_search_tree(tree, right, key, maxi)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    if not tree:
        print("CORRECT")
        return

    real_tree = build_tree(tree, 0)
    in_order(real_tree)

    if is_binary_search_tree(tree, 0, -math.inf, math.inf):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
