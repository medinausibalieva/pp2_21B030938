def new_list(args):
    x = []
    for arg in args:
        if arg not in x:
            x.append(arg)
    return x

List1 = [1, 3, 1, 1, 6, 7, 3, 6, 9, 0]
List2 = ['Medina', 'Aizhan', 'Medina', 'Daneliya', 'Aizhan', 'Daniel']
List3 = ['KBTU', '21BD', 2022, 'KBTU', '21BD']
print(new_list(List1))
print(new_list(List2))
print(new_list(List3))