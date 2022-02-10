a = []
cnt = 0
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)
    cnt += 1
b = []    
for i in range(0, cnt // 2):    
        b.append(a[i] + a[cnt - i - 1])
c = a[cnt // 2]
b.reverse()
if cnt % 2 == 1:
    b.insert(0, c)
b.reverse()    
for i in b:
    print(i, end = ' ')            




