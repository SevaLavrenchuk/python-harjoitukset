import random

def heita_muokattu_noppa(tahkot):
    return random.randint (1,tahkot)
silmäluku = 0
maksimi = int(input("Anna tahkojen yhteismäärä: "))

while silmäluku != maksimi:
    silmäluku = heita_muokattu_noppa (maksimi)
    print(silmäluku)