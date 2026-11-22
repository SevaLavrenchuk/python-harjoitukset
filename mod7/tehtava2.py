nimet = set()
while True:
    nimi = input ("Anna nimi (ohjelma lopettaa tyhjällä): ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin mainittu nimi: ")
    else:
        print("Anna uusi nimi:")
        nimet.add(nimi)
#tulostetaan kaikki mainitut nimet
print("Syötetyt nimet: ")

for nimi in nimet:
    print(nimi)