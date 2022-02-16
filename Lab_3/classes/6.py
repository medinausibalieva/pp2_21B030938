def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % 2 == 0:
            return False
    return True 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 11]     
list2 = list(filter(lambda x: is_prime(x), list1))
print(list2)         