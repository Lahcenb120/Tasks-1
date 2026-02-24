pituus = float(input("Anna kuhan pituus (cm): "))
if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen. Puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallitun mittainen.")



luokka = input("Anna hyttiluokka (LUX, A, B, C): ").strip().upper()
if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")



sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
hb = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")


vuosi = int(input("Anna vuosiluku: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")