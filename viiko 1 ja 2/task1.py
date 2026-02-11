import math

nimi = input("give your name: ")

print(f"hello, {nimi}")

nimi2 = "Ben"

print(f"hello, {nimi}")


ika = int(input("give your age:"))
lisa = 10

print("käyttäjän ikä on:", ika + lisa)

ika = float(input("give your age:"))
lisa = 10

print("käyttäjän ikä on:", ika + lisa)

pituus = float(input("give your hight:"))
paino = float(input("give your weight:"))

bmi = paino / (pituus / 100)**2

print("your BMI is:", bmi)
