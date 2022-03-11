import re

def func(text):
    patterns = 'ab{2,3}'
    if re.search(patterns, text):
        return 'YES!'
    else:
        return 'NO!'  
print(func('abb'))      
print(func('abc'))   
print(func('abbbb'))     
print(func('aaavv'))     
print(func('a'))       
