# A heap data structure


class Heap:
    def __init__(self, arr):
        assert type(arr) is list
        self.heap = arr

    def parent(self, i):
        # return the parent of i
        return i // 2

    def left_child(self, i):
        return 2 * i

    def right_child(self, i):
        return (2 * i) + 1

    def sift_up(self, i):
        while i > i and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]

    def sift_down(self, i):
        pass


