a = []
b = []
n = int(input())
for i in range(n):
    c = input().split()
    if c[0] == '1':
        a.append(c[1])
    else:
        b.append(a[0]) 
        a.pop(0)
for i in b:
    print(i, end = ' ')                 