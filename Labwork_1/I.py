n = int(input())
for x in range(n):
    x = str(input())
    if x.find("@gmail.com") != -1:
        print(x.replace("@gmail.com", ""))  
'''
здесь я использовала схему string.replace(oldvalue, newvalue), 
заменила "@gmail.com" на ""
'''          