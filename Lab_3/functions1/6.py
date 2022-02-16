def reverse(str):
    ans = []
    ans.append(str[::-1])
    for i in ans:
        for j in i:
            print(j, end = ' ')

str = input().split(' ')
reverse(str)

# We are ready -> ready are We
# Hello how are you -> you are how Hello