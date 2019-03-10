# python3
import sys


n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)
compressor = []


def getParent(table):
    global parent, compressor, rank, lines
    while table != parent[table]:
        compressor.append(table)
        table = parent[table]
    for i in compressor:
        parent[i] = parent[table]
        rank[i] = 1
    compressor = []
    return parent[table]


def merge(destination, source):
    global parent, lines, rank, ans
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    elif rank[realDestination] >= rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        if rank[realDestination] == rank[realSource]:
            rank[realDestination] += 1
    else:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
    ans = max([ans, lines[realDestination], lines[realSource]])

    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)

