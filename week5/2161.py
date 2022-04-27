from collections import deque

N = int(input())
d = deque(range(1, N + 1))

while len(d) > 0:
    print(d.popleft(), end=' ')
    if len(d) == 0:
        break
    d.append(d.popleft())
