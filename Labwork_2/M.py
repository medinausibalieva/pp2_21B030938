b = []
while True:
    a = input()
    if a == '0':
        break  
    b.append(a.split())          
b.sort(key = lambda x: (x[2], x[1], x[0]))  
for i in b:
    for x in i:
        print(x , end = ' ')
    print()
       