import random
def heita_noppa():
    return random.randint(1, 6)
# Pääohjelma
while True:
    tulos = heita_noppa()
    print("Nopan silmäluku:", tulos)
    if tulos == 6:
        break


def gallonat_litroiksi(gallonat):
    return gallonat * 3.785
while True:
    maara = float(input("Anna gallonamäärä: "))
    if maara < 0:
        print("Ohjelma lopetetaan.")
        break
    litrat = gallonat_litroiksi(maara)
    print(f"{maara} gallonaa = {litrat:.2f} litraa")



def laske_summa(lista):
    return sum(lista)
luvut = [1, 2, 3, 4, 5]
summa = laske_summa(luvut)
print("Lista:", luvut)
print("Lukujen summa:", summa)






def karsi_parittomat(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista
luvut = [1, 2, 3, 4, 5, 6, 7, 8]
karsittu = karsi_parittomat(luvut)
print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu)

