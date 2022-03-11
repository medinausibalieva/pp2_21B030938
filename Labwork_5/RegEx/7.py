import re

text = 'information_technology'

def camel(text):
    a = re.split(r'[_]', text)

    for i in range(len(a)):
        a[i] = a[i].capitalize()
    return ''.join(a)    
print(camel(text))    
