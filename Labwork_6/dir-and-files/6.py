import string, os

if not os.path.exists('files'):
    os.makedirs('files')
for letter in string.ascii_uppercase:
    with open(letter + '.txt', 'w') as f:
        f.write(letter) 