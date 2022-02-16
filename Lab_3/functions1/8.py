def has_007(n):
    count = 0
    for i in a:
        if i == 0 and count == 0:
            count += 1
        if i == 0 and count == 1:
            count += 1
        if i == 7 and count == 2:
            count += 1
    return count == 3            

a = list(map(int, input().split(','))) 
print(has_007(a))      

# has_007([1,2,4,0,0,7,5]) --> True
# has_007([1,0,2,4,0,5,7]) --> True
# has_007([1,7,2,0,4,5,0]) --> False