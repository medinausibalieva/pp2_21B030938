def filter_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

list1 = map(int, input().split())
list2 = list(filter(lambda x: filter_prime(x), list1))
print(list2)                