from math import sqrt

kokonaisluku = int(input("Anna kokonaisluku: "))
while kokonaisluku != 0:
    if kokonaisluku <0:
        print ("Virheellinen numero")
    if kokonaisluku >0:
        print(sqrt(kokonaisluku))
    kokonaisluku = int(input("Anna uusi luku:"))

print("Ohjelma lopetettu")
