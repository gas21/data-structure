# python3

import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def __init__(self):
        self.n = 0
        self.parent = []
        self.tree2 = []
        self.depth = []
        self.root = None

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.tree2 = [[] for i in range(self.n)]

        for i, j in enumerate(self.parent, 0):
            if j != -1:
                self.tree2[j].append(i)
            else:
                self.root = self.tree2[i]

    def compute_fast(self, node, n):
        if not node:
            self.depth.append(n)
            return n
        for i in node:
            self.compute_fast(self.tree2[i], n+1)


def main():
    tree = TreeHeight()
    tree.read()
    tree.compute_fast(tree.root, 1)
    print(max(tree.depth))


threading.Thread(target=main).start()
