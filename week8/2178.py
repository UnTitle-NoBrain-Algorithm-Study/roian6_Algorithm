from collections import deque
from sys import stdin

MAX = 101
N, M = map(int, stdin.readline().split())
ans = [[0 for j in range(MAX)] for i in range(MAX)]
visited = [[False for j in range(MAX)] for i in range(MAX)]
m = [[] for i in range(MAX)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()

for i in range(N):
    s = input()
    for s1 in s:
        m[i].append(s1)

cnt = 1
visited[0][0] = True
q.append((0, 0))
while len(q) > 0:
    u = q.popleft()
    x = u[0]
    y = u[1]

    for i in range(4):
        nx = u[0] + dx[i]
        ny = u[1] + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if m[nx][ny] == '1' and not visited[nx][ny]:
                ans[nx][ny] = ans[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))

print(ans[N - 1][M - 1] + 1)
