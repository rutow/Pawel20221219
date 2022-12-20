krotka = ()
krotka2 = (5,)
liczby = 3, 5, 7, 9
elem = 2,
imiona = 'Tomek','Adam','Darek'
imiona2 = 'Tomek','Adam','Darek', 'Paweł', 'Ktos'
print(krotka)
print(krotka2)
print(liczby)
print(elem)
print(imiona)

print(imiona[1])
# imie1 = imiona[0]
# imie2 = imiona[1]
# imie3 = imiona[2]
imie1, imie2, imie3 = imiona
print(imie1, imie2, imie3)

imie4, imie5, imie6, *lista = imiona2
print(imie4, imie5, imie6)
print(lista)