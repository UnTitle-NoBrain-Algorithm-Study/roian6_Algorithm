while True:
    q = []
    s = input()
    if s == '.':
        break

    for s1 in s:
        if s1 == '(':
            q.append('(')
        elif s1 == ')':
            if len(q) == 0 or q.pop() == '[':
                break
        elif s1 == '[':
            q.append('[')
        elif s1 == ']':
            if len(q) == 0 or q.pop() == '(':
                break
    else:
        if len(q) == 0:
            print('yes')
            continue
    print('no')
