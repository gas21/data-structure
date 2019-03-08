# python3
import math

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        size = len(self._data) - 1
        for j in range(size // 2, -1, -1):
            maxindex = j
            i = j
            while True:
                l, r = 2*(maxindex + 1) - 1,  2 * (maxindex + 1)
                if l <= size and self._data[l] < self._data[maxindex]:
                    maxindex = l
                if r <= size and self._data[r] < self._data[maxindex]:
                    maxindex = r
                if maxindex == i:
                    break
                self._data[i], self._data[maxindex] = self._data[maxindex], self._data[i]
                self._swaps.append((i, maxindex))
                i = maxindex

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()