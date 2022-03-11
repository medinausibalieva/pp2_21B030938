import re


def snake(text):
    a = re.findall('[A-Z][a-z]*', text)
    for i in range(len(a)):
        a[i] = a[i].lower()
    return '_'.join(a)    
print(snake('JavaScript'))
print(snake('AlmatyCity'))
print(snake('InformationTechnology'))
print(snake('KbtuUni'))



     