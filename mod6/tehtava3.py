def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

gallonat = float(input("Anna gallonien määrä: "))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print ("Litramäärä: ", litrat)
    gallonat = float(input("Anna gallonien määrä: "))
