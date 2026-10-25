luvut = []

while True:
    luku = int(input("Anna arvo: "))
    if luku == 0:
        print("Ohjelma lopetetaan.")
        break
    luvut.append(luku)
    print ("Lisäysjärjestyksessä: ", luvut)
    print ("pienimmästä suurempään: ", sorted(luvut))