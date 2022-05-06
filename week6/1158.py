from collections import deque

N, K = map(int, input().split())
d = deque(range(1, N + 1))
i = 0
ans = []

while len(d) > 0:
    i += 1
    if i == K:
        ans.append(d.popleft())
        i = 0
    else:
        d.append(d.popleft())

print('<', end='')
for i, n in enumerate(ans):
    print(n, end='')
    if i + 1 != N:
        print(', ', end='')
print('>', end='')
