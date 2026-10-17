import random

maara = int(input("aprakuutioiden määrä?" ))
summa = 0

for i in range(maara):
    luku = random.randint (1,6)
    summa = summa + luku
print("Silmälukujen summa: ", summa)

