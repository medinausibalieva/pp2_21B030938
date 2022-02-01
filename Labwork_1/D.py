s = input()
a = input()
s = int(s)

if a == "k":
    b = input()
    b = int(b)
    c = s / 1024
    print(round(c, b)) 
# функция round() округляет число до цифры b
else:
    print(s * 1024)    