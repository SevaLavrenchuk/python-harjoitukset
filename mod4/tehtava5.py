

yritykset = 0

while yritykset < 5: 
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input ("Kirjoita salasana: ")

    if tunnus == "Joyful" and salasana == "9876":
        print ("Tervetuloa")
        break
    else:
        print ("Väärä käyttäjätunnus tai salasana") 
        yritykset = yritykset + 1

if yritykset == 5:
    print("Pääsy evätty")
    