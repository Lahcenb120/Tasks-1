raha = float(input("kuinka paljon sinulla rahaa? "))

if raha >= 5:
    print("voit ostaa kahvin")

print("kiitos hei!")

a = True
b = False

if a and b:
    print("both are correct")

if a or be:
    print("the other answer is correct")

if not a and b:
    print("not correct")


raha = float(input("kuinka paljon sinulla raha? "))
if raha >= 5:
    print("here is your coffee")
else:
    puuttuva = 5 - raha
    print("sorry, sinulta puuttuu", puuttuva)
print("kiitos hei!")

numero = int(input("anna kokonaisluku: "))
if numero > 0:
    print("luku on positiivinen")
elif numero < 0 :
    print("luku on negatiivinen")
else:
    print("numero oli 0")

ika = int(input("kuinka vanha olet? "))
if ika >= 65:
    print("olet eläkeissä")
elif ika >= 18:
    print("työikäinen")
elif ika >= 7:
    print("olet koululainen")
else:
    print("you are still a small child")


numero = int(input("anna luku: "))
if numero > 0:
    if numero % 2 == 0:
        print("luku on parillinen")
    else:
        print("luku on pariton")
else:
    print("numero joka annoit oli negatiivinen")
print("jatketaan!")


numero = int(input("anna kokonaisluku: "))
if numero < 0:
    float(print(numero * -1))
else:
    print(numero)
    