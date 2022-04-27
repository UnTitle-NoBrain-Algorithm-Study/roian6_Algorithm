from sys import stdin
from collections import deque

N = int(stdin.readline())
st = deque()

for i in range(N):
    s = stdin.readline().strip()

    if 'push' in s:
        st.append(s.split()[1])
    elif 'pop' == s:
        print(-1 if len(st) == 0 else st.pop())
    elif 'size' == s:
        print(len(st))
    elif 'empty' == s:
        print(1 if len(st) == 0 else 0)
    elif 'top' == s:
        print(-1 if len(st) == 0 else st[-1])
