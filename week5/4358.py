from sys import stdin

d = {}
li = []
n = 0

while True:
    s = stdin.readline().strip()
    if not s:
        break
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
        li.append(s)
    n += 1

li.sort()

for s in li:
    print(f'{s} {d[s] / n * 100:.4f}')
