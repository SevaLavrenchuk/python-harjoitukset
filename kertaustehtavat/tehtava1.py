tuntipalkka = int(input("Anna tuntipalkka: "))
tunnit = float(input("Tehdyt tunnit: "))
viikonpaiva = input("Viikonpäivä: ")
päiväpalkka = tuntipalkka * tunnit
if viikonpaiva == "sunnuntai":
    päiväpalkka = päiväpalkka * 2,
print ("Päiväpalkkasi on:", päiväpalkka, "e")


