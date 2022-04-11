n = int(input())

li = [0, 1]
for i in range(90):
    li.append(li[i] + li[i + 1])

print(li[n])
