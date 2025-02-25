n = int(input())

lst = [0, 1]
for nn in range(2, n+1):
    lst.append(lst[nn-1] + lst[nn-2])

print(lst[n])
    