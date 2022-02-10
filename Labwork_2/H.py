a, b = input().split()
n = int(input())
pair = []
dis = []
for i in range(n):
    num = input()
    pair.append(num.split())
for x in pair:
    d = ((int(a) - int(x[0]))**2 + (int(b) - int(x[1]))**2)**(1/2)
    dis.append(d)
dis.sort()    
for y in dis:
    for x in pair:
        if y == ((int(a) - int(x[0]))**2 + (int(b) - int(x[1]))**2)**(1/2):
            print(x[0], x[1])
            pair.remove(x)