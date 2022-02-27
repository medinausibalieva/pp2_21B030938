import math

def area(tr):
    ans = (tr['first'] + tr['second'])/2 * tr['height']
    print(ans)

trapezoid = {
    'height': 5,
    'first': 5,
    'second': 6
}
area(trapezoid)