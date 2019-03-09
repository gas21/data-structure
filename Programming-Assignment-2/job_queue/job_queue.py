# python3
import heapq
import copy


class JobQueue:
    def __init__(self):
        self.num_workers = None
        self.jobs = None
        self.assigned = None  # assigned worker, start time
        self.assigned_workers = None

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.assigned_workers = [[0, i] for i in range(self.num_workers)]
        self.assigned = []
        assert m == len(self.jobs)

    def write_response(self):
        for i in self.assigned:
            print(i[1], i[0])

    def assign_jobs(self):
        heapq.heapify(self.assigned_workers)
        for i in self.jobs:
            a = heapq.heappop(self.assigned_workers)
            self.assigned.append(copy.deepcopy(a))
            a[0] += i
            heapq.heappush(self.assigned_workers, a)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
