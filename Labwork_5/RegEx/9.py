import re 

text = 'HelloHowAreYou'
a = re.findall('[A-Z][a-z]*', text)
b = ' '.join(a)
print(b)