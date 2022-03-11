import re

def func(text):
    patterns = '^a(b*)$'
    if re.search(patterns, text):
        return 'YES!'
    else:
        return 'NO'  
print(func('ab'))      
print(func('abc'))   
print(func('abbbb'))         
print(func('a'))       
