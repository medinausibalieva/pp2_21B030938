import re

def func(text):
    patterns = 'a.*b$'
    if re.search(patterns, text):
        return 'found a match!'
    else:
        return 'not matched'    
print(func('a56hnby78'))  
print(func('a56hnby788'))  
print(func('aaudhcbb'))
print(func('dva56hnby788b'))    