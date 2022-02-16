def calc(numheads, numlegs):
    a = numheads * 2    
    # рассматриваем вариант когда все животные курицы (*2)
    b = numlegs - a
    # Узнаем, сколько лишних ног, так как среди животных есть кролики
    c = 4 - 2   # узнаем на сколько ног у кролика больше, чем у курицы
    rabbits = b / c
    chickens = numheads - rabbits
    print(int(rabbits), int(chickens))

numheads, numlegs = map(int, input().split())
calc(numheads, numlegs)