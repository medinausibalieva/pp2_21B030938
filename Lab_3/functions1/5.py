import itertools

def permutation(string):
    l = list(string)
    p = list(itertools.permutations(l))
    print([''.join(permutation) for permutation in p])
     
    # ['SUN', 'SNU', 'USN', 'UNS', 'NSU', 'NUS']

s = str(input())
permutation(s)

