import re 

def func(text):
    print(re.sub('[, .]', ':', text))
func('Hello, my name is Medina.')    