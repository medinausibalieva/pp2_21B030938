s = input()

def findlen(str):
    cnt = 0
    for i in str:
        cnt += 1
    return cnt
word = ''
ans = ''
for i in range(len(s)):
    if s[i] != ' ':
        word = word + s[i]
    if s[i] == ' ':
        if findlen(word) >= 3:
            ans = ans + word + ' '
        word = ''    
    if i == len(s) - 1:
        if findlen(word) >= 3:
            ans = ans + word
print(ans)                    