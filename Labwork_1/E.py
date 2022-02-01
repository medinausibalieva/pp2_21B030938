a, b = input().split()
a = int(a)
b = int(b)
flag = True
if a > 1:
    for i in range(2, a // 2 + 1): #я написала (a//2 + 1), потому что учитываем (a//2)
        if a % i == 0:
            flag = False
            break
if a < 500 and flag and b % 2 == 0:
    print("Good job!")
else:
    print("Try next time!")            
