def squares(n):
    for x in range(n):
        wynik = x ** 2
    return wynik

def squares_gen(n):
    for x in range(n):
        yield x ** 2
sg = squares_gen(4)
print(next(sg))
print(next(sg))
print(next(sg))
print(next(sg))

def counter(start=0):
    n = start
    while True:
        yield n
        n += 1

c = counter()
lista = [next(c), next(c), 2022, next(c), next(c), 2022]
print(lista)
print(next(c))