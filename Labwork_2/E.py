s = list(map(int, input().split(' ')))
cnt = 0
if len(s) == 1:
    a = int(input())
    for i in range(s[0]):
        i = a + 2 * i 
        cnt ^= i
else:
    for x in range(s[0]):
        x = s[1] + 2 * x
        cnt ^= x
print(cnt)    
