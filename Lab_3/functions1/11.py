def is_Palindrome(str):
    for i in range(0, len(str) // 2):
        if str[i] != str[len(str) - 1 - i]:
            return False
    return True

s = str(input())
print(is_Palindrome(s))   

# (madam) -> True
# (kayak) -> true
# (Almaty) -> False