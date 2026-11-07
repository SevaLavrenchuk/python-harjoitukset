def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

#Pääohjelma
testilista = [1, 4, 6, 13]
tulos = laske_summa(testilista)

print("Lukujen summa on: ", tulos)