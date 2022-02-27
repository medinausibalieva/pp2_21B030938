def my_gen(n):
    for i in range(n):
        yield (i ** 2)

for x in my_gen(10):
    print(x, end = ' ')       