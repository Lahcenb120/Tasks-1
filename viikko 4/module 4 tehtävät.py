luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1


while True:
    tuumat = float(input("Anna tuumat: "))
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa = {senttimetrit:.2f} cm")

pienin = None
suurin = None

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luku = float(syote)
    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku
print("Pienin luku:", pienin)
print("Suurin luku:", suurin)



import random
salainen_luku = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku 1-10: "))
    if arvaus > salainen_luku:
        print("Liian suuri arvaus")
    elif arvaus < salainen_luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break




oikea_tunnus = "python"
oikea_salasana = "rules"
yritykset = 0
while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana")
        yritykset += 1
if yritykset == 5:
    print("Pääsy evätty")



import random
N = int(input("Anna arvottavien pisteiden määrä: "))
n = 0
laskuri = 0
while laskuri < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    laskuri += 1
pii = 4 * n / N
print("Piin likiarvo on:", pii)