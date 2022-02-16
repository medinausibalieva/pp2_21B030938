def recipe(dict):
    for value, key in (dict.items()):
        print(int(key) * 28.3495231) 

ingredients = {
    'milk': 250,
    'sugar': 300,
    'flour': 400,
    'apple': 150,
    'kefir': 100
}
recipe(ingredients)
