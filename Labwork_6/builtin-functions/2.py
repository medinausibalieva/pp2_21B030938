
s = 'Hello! Have a Wonderful Weekends'

lower = 0
upper = 0
for i in s:
    if i.islower():
        lower += 1
    if i.isupper():
        upper += 1
print('Number of upper case letters:', upper)    
print('Number of lower case letters:', lower)       