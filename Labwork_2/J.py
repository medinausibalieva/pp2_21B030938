n = int(input())
d = []
for i in range(n):
    s = str(input())
    for x in s :
        if(any(x.islower() for x in s) and any(x.isdigit() for x in s) and any(x.isupper() for x in s)):
            d.append(s)
d = set(d)
d = list(d)    
d.sort()        
print(len(d))
for i in d: 
    print(i)           
