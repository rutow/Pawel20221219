# lista = [4, 6, 8, 0]
#
# for liczba in lista:
#     print(liczba)
# #dla iteratora w liscie wydrukuj iterator
#
# for i in range(10, 20, 2):
#     print(i)
# #
# liczba = list(range(1, 11, 2))
# print(liczba)
#
# imiona = ['Tomek', 'Bartek', 'Ania', 'Paweł']
# lata = [23, 22, 21]
# for p in range(len(imiona)):
#     print(p, imiona[p])

# for poz, imie in enumerate(imiona):
#     wiek = lata[poz]
# #     print(imie, wiek)
#
# for person, age in zip(imiona, lata):
#     print(person, age)

for i in range(1,6):
    for j in range(1, i + 1):
        print("*", end="")
    print()