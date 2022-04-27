from collections import Counter
from sys import stdin

N = int(stdin.readline())
li = [0] * N

for i in range(N):
    li[i] = int(stdin.readline())
li = sorted(li)

print(round(sum(li) / N))
print(li[int(N / 2)])

if len(li) == 1:
    print(li[0])
else:
    count = Counter(li)
    most2 = count.most_common()
    most = most2[1][0] if most2[0][1] == most2[1][1] else most2[0][0]
    print(most)

print(li[-1] - li[0])
