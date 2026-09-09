import math
leiviskat = int(input("Anna leiviskat: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))
leiviska = 20 * naulat
naula = 32 * luodit
luoti = 13.3
kaikki_luodit = (leiviskat * 20 * 32) + (naulat * 32) + luodit
kokonaisgrammat = kaikki_luodit * 13.3
kilogrammat = int(kokonaisgrammat / 1000)
grammat = kokonaisgrammat % 1000
print ("Massa nykymittojen mukaan on: ")
print (kilogrammat, "kg", grammat, "g")