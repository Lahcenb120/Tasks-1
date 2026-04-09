vuodenajat = (
    "talvi", "talvi", "kevät",
    "kevät", "kevät", "kesä",
    "kesä", "kesä", "syksy",
    "syksy", "syksy", "talvi"
)

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print("Vuodenaika on:", vuodenajat[kuukausi - 1])
else:
    print("Virheellinen kuukausi!")





nimet = set()

while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nSyötetyt nimet:")
for n in nimet:
    print(n)





lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Lisää uusi lentoasema")
    print("2 = Hae lentoasema")
    print("3 = Lopeta")

    valinta = input("Valintasi: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        print("Ohjelma lopetettu.")
        break

    else:
        print("Virheellinen valinta!")

