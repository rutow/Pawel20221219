def funkcja(x):
    return x * 2


fun = lambda x: x * 2

print(f"Wynik dzialania funkcji {funkcja(5)}")
print(f"Wynik dzialania funkcji {funkcja(15)}")
print(f"Wynik dzialania funkcji {funkcja(25)}")
print(f"Wynik dzialania funkcji {fun(30)}")

wiek = lambda x: "dziecko" if x < 10 else ("Nastolatek" if x < 18 else "Dorosly")
print(wiek(5))
print(wiek(15))
print(wiek(25))