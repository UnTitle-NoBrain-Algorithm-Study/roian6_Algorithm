N = int(input())
M = int(input())
li = []
ans = [False, True] + [False for i in range(100)]

for i in range(M):
    li.append(sorted(tuple(map(int, input().split()))))
li = sorted(li)

for i in range(100):
    for t in li:
        if ans[t[0]] or ans[t[1]]:
            ans[t[0]] = True
            ans[t[1]] = True

print(ans.count(True) - 1)
