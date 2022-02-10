a, b = input().split('+')
arr1 = []
arr2 = []
for i in range(len(a)//3):
    arr1.append(a[i*3:i*3+3])
for i in range(len(b)//3):
    arr2.append(b[i*3:i*3+3])
def f1(list):
    for i in range(len(list)):
        if list[i] == 'ONE':
            list[i] = 1
        if list[i] == 'TWO':
            list[i] = 2
        if list[i] == 'THR':
            list[i] = 3
        if list[i] == 'FOU':
            list[i] = 4
        if list[i] == 'FIV':
            list[i] = 5
        if list[i] == 'SIX':
            list[i] = 6
        if list[i] == 'SEV':
            list[i] = 7
        if list[i] == 'EIG':
            list[i] = 8
        if list[i] == 'NIN':
            list[i] = 9
        if list[i] == 'ZER':
            list[i] = 0
f1(arr1)
f1(arr2)
sum = []
def f2(c1, c2, c):
    s1 = 0
    s2 = 0
    for i in range(len(c1)):
        s1 += int(c1[i])*pow(10, len(c1) - i - 1)
    for j in range(len(c2)):
        s2 += int(c2[j])*pow(10, len(c2) - j - 1)
    c.append(s1 + s2)   
f2(arr1, arr2, sum)

str = [str(w) for w in sum]
ans = []
def f3(ans1, ans2):
    for i in range(len(ans1[0])):
        if ans1[0][i] == '1':
            ans2.append('ONE')
        if ans1[0][i] == '2':
            ans2.append('TWO')
        if ans1[0][i] == '3':
            ans2.append('THR')
        if ans1[0][i] == '4':
            ans2.append('FOU')
        if ans1[0][i] == '5':
            ans2.append('FIV')
        if ans1[0][i] == '6':
            ans2.append('SIX')
        if ans1[0][i] == '7':
            ans2.append('SEV')
        if ans1[0][i] == '8':
            ans2.append('EIG')
        if ans1[0][i] == '9':
            ans2.append('NIN')                               
        if ans1[0][i] == '0':
            ans2.append('ZER')
f3(str, ans)
for i in range(len(ans)):
    print(ans[i], end = '')            
