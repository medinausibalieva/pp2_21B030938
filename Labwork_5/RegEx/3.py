import re

def func(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, text):
        return 'found a match!'
    else:
        return 'Not matched'    
print(func('apple_pineapple'))
print(func('apple_Banana'))
print(func('melon_Pineapple'))
print(func('Melon_pineapple'))
print(func('apple_melon'))
