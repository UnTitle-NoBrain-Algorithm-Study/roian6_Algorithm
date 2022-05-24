N = int(input())
ans = ''

for i in range(N * 2):
    for j in range(N):
        print('*' if (i % 2 + j % 2) % 2 == 0 else ' ', end='')
    print()
