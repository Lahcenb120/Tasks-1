print("Hei, Viivi Virta!")


nimi = input("Anna nimesi: ")
print(f"Terve, {nimi}!")


import math
r = float(input("Anna ympyrän säde: "))
ala = math.pi * r * r
print(f"Pinta-ala on {ala:.2f}")



kanta = float(input("Anna kanta: "))
korkeus = float(input("Anna korkeus: "))

piiri = 2 * (kanta + korkeus)
ala = kanta * korkeus

print(f"Piiri on {piiri:.2f}")
print(f"Pinta-ala on {ala:.2f}")



a = int(input("Anna kokonaisluku 1: "))
b = int(input("Anna kokonaisluku 2: "))
c = int(input("Anna kokonaisluku 3: "))

summa = a + b + c
tulo = a * b * c
keskiarvo = summa / 3

print(f"Summa: {summa}")
print(f"Tulo: {tulo}")
print(f"Keskiarvo: {keskiarvo}")




leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("\nAnna naulat.\n"))
luodit = float(input("\nAnna luodit.\n"))

luoteja_yht = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat = luoteja_yht * 13.3

kilot = int(grammat // 1000)
grammat_jaljella = grammat - kilot * 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {grammat_jaljella:.2f} grammaa.")



import random
num3 = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
num4 = f"{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}"

print("Kolminumeroinen koodi:", num3)
print("Nelinumeroinen koodi:", num4)