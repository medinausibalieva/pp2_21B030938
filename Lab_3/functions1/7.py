def has_3_3(n):
    for i in range(len(n)-1):
        if n[i:i+2] == [3, 3]:
            return True
    return False 

a = list(map(int, input().split(',')))
print(has_3_3(a)) 

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False