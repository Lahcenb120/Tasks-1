import random

n = int(input("Kuinka monta arpakuutiota heitetään? "))
summa = 0

for i in range(n):
    luku = random.randint(1, 6)
    summa += luku

print("Silmälukujen summa on:", summa)


luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(int(syote))

luvut.sort(reverse=True)

for luku in luvut[:5]:
    print(luku)


luku = int(input("Anna kokonaisluku: "))
alkuluku = True

for i in range(2, luku):
    if luku % i == 0:
        alkuluku = False
        break

if alkuluku and luku > 1:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")


kaupungit = []

for i in range(5):
    nimi = input("Anna kaupungin nimi: ")
    kaupungit.append(nimi)

for kaupunki in kaupungit:
    print(kaupunki)