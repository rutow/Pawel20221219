# indeks = int(input('Podaj miejsce wstawienia:'))
# cyfra = input('Podaj ocenę z klasówki:')
import random

oceny = [5, 3, 5, 4, 4, 2, 1, 4, 3, 3, 4]
# print(len(oceny))
# print(oceny[:5])
print("Ilosc trojek w ocenach", oceny.count(3))
print(oceny)
#oceny.insert(indeks, int(cyfra))
oceny.append(6) #dodaje zawsze na końcu listy
oceny.remove(1) #usuwa 1

print(oceny)
oceny.pop() # usuwa ostanie element
print(oceny)
oceny.sort()
print(oceny)
oceny.reverse()
print(oceny)

oceny[-1] = 3 # -1 oznacza że liczymy od końca
print(oceny)

dziennik = tuple(oceny)
print(dziennik)
oceny = list(dziennik)
print(oceny)
#oceny[-1] = 33
oceny2 = oceny.copy()
oceny[-1] = 33
print("Oceny2", oceny2)
loteria = random.choice(oceny)
print("Wylosowana liczba z tabeli ocen", loteria)

kostka6 = random.randint(1, 6)
print("Wynik rzutu kostką:", kostka6)
print(random.random())

losowe_wartosci = []
losowe_wartosci.append(int(random.random()*1000))
losowe_wartosci.append(int(random.random()*1000))
print(losowe_wartosci)