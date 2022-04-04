from sys import stdin
from collections import deque

N = int(stdin.readline())
li = [''] * N
for i in range(N):
    li[i] = f'{(int(stdin.readline()) + 1000000):07d}'

# Radix
for i in range(1, 8):
    buck = [deque() for j in range(10)]
    for s in li:
        n = int(s[-i])
        buck[n].append(s)
    li = []
    for j in range(10):
        li.extend(buck[j])

for i in range(N):
    print(int(li[i]) - 1000000)
