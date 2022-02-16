def histogram(a):
    ans = ''
    for i in range(len(a)):
        t = a[i]
        while t > 0:
            ans += '*'
            t -= 1
        print(ans)        
l = list(map(int, input().split(',')))
histogram(l)      

# histogram([4, 9, 7])
# ****
# *********
# *******