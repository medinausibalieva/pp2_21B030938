# Task condition: The recipe you are reading indicates how many grams you need for the ingredient. 
# Check the gram of each ingredient for a prime number. 
# Unfortunately, your store only sells items in ounces.
#  Create a function to convert grams to ounces, and output only prime numbers in units.  ounce = 28.3495231 * grams

def filter_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def recipe(dict):
    for value, key in (dict.items()):
        if filter_prime(key):
            print(value, ':', int(key) * 28.3495231) 

ingredients = {
    'milk': 253,
    'sugar': 333,
    'flour': 400,
    'apple': 151,
    'kefir': 103,
    'sour cream': 179,
    'cinnamon': 250
}

recipe(ingredients)