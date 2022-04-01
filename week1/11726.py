n = int(input())

a = 1
b = 2

if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
    print(b % 10007)
