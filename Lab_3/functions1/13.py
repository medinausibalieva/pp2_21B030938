print('Hello! What is your name?')    
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
print('Take a guess.')   
num = int(input())     

import random

a = random.randint(1, 20)
cnt = []
def func(num):
    if num != a:
        print('Your guess is too low.')
        print('Take a guess.')
        b = int(input())
        cnt.append(int(1)) 
        return func(b)   
    else:
         print('Good job ' + name + '! You guessed my number in ' + str(len(cnt) + 1) + ' guesses!')
func(num)         