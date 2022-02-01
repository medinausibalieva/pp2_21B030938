s = str(input())
sum = 0
for x in s:
    sum += ord(x)
"""
 я использовала функцию ord(), так как он нам дает 
ascii code символа
 """    
if sum > 300:
    print("It is tasty!")
else:
    print("Oh, no!") 