n = int(input())

for i in range(n):
    i = int(input()) 
    if i <= 10:
        print("Go to work!")
    if i > 10 and i <= 25:
        print("You are weak")    
    if i > 25 and i <= 45:
        print("Okay, fine")
    if i > 45:
        print("Burn! Burn! Burn Young!")   