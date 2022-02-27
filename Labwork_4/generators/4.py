a, b = 4, 10
items= []
for it in range(a, b):
    items.append(it**2)

it = iter(items)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
