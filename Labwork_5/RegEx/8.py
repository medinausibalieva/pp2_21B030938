import re 

text = 'HelloHowAreYou'
print(re.findall('[A-Z][a-z]*', text))