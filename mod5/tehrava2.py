maara = input("Anna luku:")
luvut = []
while maara != "":
    luku = int(maara)
    luvut.append(luku)
    maara = input("Anna uusi luku: ")
luvut.sort(reverse=True)
print("5 suurinta lukua:", luvut[:5])
