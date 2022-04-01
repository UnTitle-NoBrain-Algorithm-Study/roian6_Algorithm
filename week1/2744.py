s = input()
ans = ''

for s1 in s:
    if s1.isupper():
        ans += s1.lower()
    elif s1.islower():
        ans += s1.upper()

print(ans)
