# A, B = map(int, input().split())
#
# print(A + B)

A, B = input().split()
ans = ''
one = 0

min_len = min((len(A), len(B)))
max_len = max((len(A), len(B)))

for i in range(1, min_len + 1):
    su = int(A[-i]) + int(B[-i]) + one
    one = su // 10
    ans += str(su % 10)

if max_len != min_len:
    left = int(str(max(int(A), int(B)))[:max_len - min_len]) + one
    ans = str(left) + ans[::-1]
else:
    if one == 1:
        ans += '1'
    ans = ans[::-1]

print(ans)
