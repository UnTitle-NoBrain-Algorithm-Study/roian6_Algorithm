S = input()
b = False
ans = ''
word = ''

for s in S:
    if s == '<':
        b = True
        ans += word[::-1]
        word = ''
    elif s == '>':
        b = False
        ans += '>'
        continue
    elif s == ' ':
        ans += word[::-1]
        word = ''
        ans += ' '
        continue

    if b:
        ans += s
    else:
        word += s

ans += word[::-1]
print(ans)
