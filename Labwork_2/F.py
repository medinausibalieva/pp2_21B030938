n = int(input())
dic = dict()
for i in range(n):
    name, pay = map(str, input().split())
    if name in dic:
        dic[name] = dic[name] + int(pay)
    else:
        dic[name] = int(pay)
i = dic.values()
maxi = max(i)
for key,value in sorted (dic.items()):
    if value == maxi:
        print(f'{key} is lucky!')
    else:
        print(f'{key} has to receive {maxi - int(value)} tenge')    
