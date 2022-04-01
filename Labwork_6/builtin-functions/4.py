from time import sleep
import math

def func(n, milliseconds):
    sleep(milliseconds/1000)
    return math.sqrt(n)

n = int(input())
milliseconds = int(input())
ans = func(n, milliseconds)

print('Square root of', n, 'after', milliseconds, 'millisecond is', ans)