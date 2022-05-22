from collections import deque
from sys import stdin

N, M, R = map(int, stdin.readline().split())
ans = [0] * N
visited = {}
d = {}
q = deque()

for i in range(1, N + 1):
    visited[i] = False
    d[i] = []

for i in range(M):
    a, b = map(int, stdin.readline().split())
    d[a].append(b)
    d[b].append(a)

cnt = 1
q.append(R)
while len(q) > 0:
    u = q.pop()
    if not visited[u]:
        visited[u] = True
        ans[u - 1] = cnt
        cnt += 1
        for n in sorted(d[u], reverse=True):
            if not visited[n]:
                q.append(n)

for n in ans:
    print(n)
