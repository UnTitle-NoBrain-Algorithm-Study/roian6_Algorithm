s = input()
if len(s) == 1:
    print(0.0)
else:
    ans = ord('E') - ord(s[0])
    if s[1] == '+':
        ans += 0.3
    elif s[1] == '-':
        ans -= 0.3
    print(f'{ans:.1f}')
