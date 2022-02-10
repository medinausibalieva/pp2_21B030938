a = int(input())
dic = dict()
for i in range(a):
    demon, weak = input().split()
    if weak in dic:
        dic[weak] += 1
    else:
        dic[weak] = 1
b = int(input())
for i in range(b):
    hunter, abil, num = input().split()
    if abil in dic:
        if dic[abil] > int(num):
          dic[abil] -= int(num)
        else:
          dic[abil] = 0
sum = 0
for i in dic:
    if dic[i] != 0:
        sum += dic[i]
print('Demons left:', sum)                
