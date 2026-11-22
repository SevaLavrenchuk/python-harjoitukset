#vuodenajat monikkotietorakenteessa
vuodenajat = ("talvi", "kevät", "kesä", "syksy")

#vuodenajat kuukausina
talvi = ("joulukuu", "tammikuu", "helmikuu")
kevät = ("maaliskuu", "huhtikuu", "toukokuu")
kesä = ("kesäkuu", "heinäkuu", "elokuu")
syksy = ("syyskuu", "lokakuu", "marraskuu")

#kysytään kuukausi
kuukausi = int(input("Anna kuukauden nro (1-12): "))
#selvitetään vuodenaika
if kuukausi in (12,1,2):
    print (vuodenajat[0])
elif kuukausi in (3,4,5):
    print (vuodenajat[1])
elif kuukausi in (6,7,8):
    print (vuodenajat[2])
elif kuukausi in (9,10,11):
    print (vuodenajat[3])
else:
    print ("Virheellinen kuukauden numero!")