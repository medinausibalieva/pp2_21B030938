sweets = ['ice-cream', 'chocolate', 'lolipop', 'cooky']

with open('input_1.txt', 'w') as f:
    for i in sweets:
        f.write(f'{i}\n')
content = open('input_1.txt')
print(content.read())
