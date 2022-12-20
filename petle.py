# znaPythona = False
#
# if znaPythona:
#     print("Gratulacje!")
# else:
#     print("Musisz sie nauczyć")
# #
# # print("...Kolejne instrukcje programu...")
#
#
# znaPythona = input("Czy znasz język? (Wprowadź 't' lub 'n'):")
#
# if znaPythona == 'tak' or znaPythona == 'Tak' or znaPythona == 'TAK' or znaPythona == 'T':
#     print("Gratulacje")
# elif znaPythona == 'n' or znaPythona == 'nie' or znaPythona == 'N':
#     print("Musisz się nauczyć")
# else:
#     print("Nie ma takiego wyboru")
#
# print("...Kolejne instrukcje programu...")
#
#
# podatek = 1000
# if podatek <= 1000:
#     oplata = 0.0
# elif podatek < 3000:
#     oplata = 0.2
# elif podatek < 5000:
#     oplata = 0.35
# else:
#     oplata = 0.45
#
# print(oplata)
#
#
zmaowienie = 247

# if zmaowienie > 100:
#     rabat = 0.10
# else:
#     rabat = 0.0
#
# print(f"Twoje zamowiene na kwote {zmaowienie} otrzymuje rabat w wysokosci: {rabat}")
#
#
# rabat = 0.1 if zmaowienie > 100 else 0.0
# print(f"Twoje zamowiene na kwote {zmaowienie} otrzymuje rabat w wysokosci: {rabat}")


alert = 'email'
error = 'medium'
message = 'warning'

if alert == 'console':
    print(message)
elif alert == 'email':
    if error == 'critical':
        print("Wysyłam maila ...")
    elif error == 'medium':
        print("Wysyłam mniej ważnego maila")
    else:
        print("Wysyłam maila ale później")
else:
    print("Błędny status alertu")
