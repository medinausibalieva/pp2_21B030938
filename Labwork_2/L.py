s = input()
def func(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
    return len(text) == 0
if func(s):
    print('Yes')
else:
    print('No')            