def divisible(n):
    for x in range(n):
        if x % 3 == 0 and x % 4 == 0:
            yield x
n = int(input())
for x in divisible(n):
    print(x)