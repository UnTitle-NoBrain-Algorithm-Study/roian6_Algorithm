N = int(input())
ans = 0

while N > 0:
    if N % 5 == 0:
        ans += int(N / 5)
        N = 0
        break
    N -= 3
    ans += 1

print(ans if N == 0 else -1)
