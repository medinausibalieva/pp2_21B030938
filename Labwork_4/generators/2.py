def my_gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

n = int(input())
a = list(my_gen(n))
for i in range(len(a)):
    if i != len(a) - 1:
        print(a[i], end = ', ')
    else:
        print(a[i])    
