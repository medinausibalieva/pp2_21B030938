s = input()
s = list(set(s.split()))
s.sort()
print(len(s))
for i in s:
    if i.isalpha():
        print(i)
    else:
        print(i[:-1])    