import re

def func(text):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return 'found a match!'
    else:
        return 'not matched'    
print(func('Almaty'))
print(func('AsTaNa'))
print(func('KBTU'))
print(func('green'))
print(func('Python'))
     