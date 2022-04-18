N = int(input())
li = []

for i in range(N):
    li2 = input().split()
    li.append([-int(li2[1]), int(li2[2]), -int(li2[3]), li2[0]])

li.sort()

for s in li:
    print(s[3])
