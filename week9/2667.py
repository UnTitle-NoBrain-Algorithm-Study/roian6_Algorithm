from collections import deque
from sys import stdin

N = int(stdin.readline())
m = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    m.append(list(map(int, stdin.readline().strip())))


def bfs(g, a, b):
    n = len(g)
    q = deque()
    q.append((a, b))
    g[a][b] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if m[nx][ny] == 1:
                    g[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1
    return cnt


ans = []
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            ans.append(bfs(m, i, j))

print(len(ans))
ans.sort()
for n in ans:
    print(n)
