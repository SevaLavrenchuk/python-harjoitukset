komento = input("Anna uusi komento: ")

while komento != "lopeta":
    print("Suoritetaan komento:", komento)
    komento = input("Anna uusi komento: ")

print("Ohjelma loppuu.")

# while tarvitsee 3 asiaa:
# 1. aloitusarvo (luku = 1)
# 2. ehto, joka kertoo milloin jatketaan (while luku <= 1000)
# 3. muuttujan muuttaminen silmukan sisällä (luku = luku+1)