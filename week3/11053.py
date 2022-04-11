N = int(input())
li = list(map(int, input().split()))
le = [1] * len(li)

for i in range(N):
    for j in range(i):
        if li[j] < li[i]:
            le[i] = max(le[i], le[j] + 1)

print(max(le))
