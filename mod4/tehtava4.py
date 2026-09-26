import random
luku = random.randint (1,10)
arvaus = int(input("Anna luku 1-10: "))

while arvaus != luku:
    if arvaus < luku:
        print ("Liian pieni arvaus. Arvaa uudestaan!")
    if arvaus > luku:
        print ("Liian suuri arvaus. Arvaa uudestaan!")
    arvaus = int(input("Arvaa uudestaan!"))
print("Oikein!")
