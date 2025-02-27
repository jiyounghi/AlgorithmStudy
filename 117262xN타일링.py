n = int(input())

t = [0, 1, 2]
for i in range(3, n+1):
    t.append((t[i-1] + t[i-2]) % 10007)
    
print(t[n])