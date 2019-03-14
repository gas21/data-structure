# python3

class HashChains:

    def __init__(self, no_of_bs):
        self.m = no_of_bs
        self.bs = [[] for _ in range(no_of_bs)]

    def hash_value(self, s):
        code = 0
        for i in reversed(s):
            code = (code * 263 + ord(i)) % 1000000007
        return code % self.m

    def add(self, _str):
        n = self.hash_value(_str)
        b = self.bs[n]
        if _str not in b:
            self.bs[n] = [_str] + b

    def delete(self, _str):
        n = self.hash_value(_str)
        b = self.bs[n]
        for i in range(len(b)):
            if b[i] == _str:
                b.pop(i)
                break

    def find(self, _str):
        n = self.hash_value(_str)
        if _str in self.bs[n]:
            return "yes"
        return "no"

    def check(self, i):
        return self.bs[i]


def query_processor(queries):
    for query in queries:
        a, b = query.split()
        if a == "add":
            HC.add(b)
        elif a == "del":
            HC.delete(b)
        elif a == "find":
            print(HC.find(b))
        elif a == "check":
            b = int(b)
            print(" ".join(HC.check(b)))


if __name__ == '__main__':
    no_of_bs = int(input())
    n = int(input())
    HC = HashChains(no_of_bs)
    queries = [input() for i in range(n)]
    query_processor(queries)

