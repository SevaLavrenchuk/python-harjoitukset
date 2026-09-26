syote = input("Anna luku: ")
ensimmainen = True

while syote != "":
    luku = int(syote)

    if ensimmainen:
        pienin = luku
        suurin = luku 
        ensimmainen = False
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    syote = input ("Anna uusi luku: ")

print (pienin, suurin)