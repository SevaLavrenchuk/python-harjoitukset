import math
def pizzan_yksikkohinta (halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade ** 2
    pinta_ala_m2 = pinta_ala/10000

    return hinta / pinta_ala_m2

#Pääohjelma


print("Pizza-vertailu")
halkaisija1 = float(input("Anna 1. pizzan halkaisija (cm): "))
hinta1 = float(input("Anna 1. pizzan hinta (e): "))

halkaisija2 = float(input("Anna 2. pizzan halkaisija (cm): "))
hinta2 = float(input("Anna 2.pizzan hinta (e): "))

pizza1 = pizzan_yksikkohinta (halkaisija1, hinta1)
pizza2 = pizzan_yksikkohinta (halkaisija2, hinta2)

print(f"1. pizzan yksikköhinta on: {pizza1:.2f} e/m2")
print(f"2. pizzan yksikköhinta on: {pizza2:.2f} e/m2")

if pizza1 < pizza2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle. ")
elif pizza1 > pizza2:
    print("Toinen pizza antaa paremman vastineen rahalle. ")
else:
    print ("Molemmilla pizzoilla on sama yksikköhinta.")

