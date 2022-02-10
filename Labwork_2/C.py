n = int(input())
a = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    a[0][i] = i
for i in range(n):
    a[i][0] = i
for i in range(n):
    for j in range(n):
        if i != 0 and j != 0:
            if i == j:
                a[i][j] = i * j
            else:
                a[i][j] = 0    
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()                