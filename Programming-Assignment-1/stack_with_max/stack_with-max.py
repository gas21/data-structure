#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        if self.__stack and a < self.__stack[-1][1]:
                self.__stack.append((a, self.__stack[-1][1]))
        else:
            self.__stack.append((a, a))

    def Pop(self):
        assert self.__stack
        self.__stack.pop()

    def Max(self):
        assert self.__stack
        return self.__stack[-1][1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
