#luon ensin lentoasema-sanakirjan
lentoasemat = {}

while True:

    valinta = input("Valitse vaihtoehto: (1. Hae uusi lentokenttä 2. Hae lentoaseman tiedot 3. Lopeta)")
    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi:")
        nimi = input("Anna lentoaseman nimi:")
        lentoasemat[icao] = nimi

    elif valinta == "2":
        icao = input("Anna lentoaseman ICAO-koodi:")
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei lötynyt.")
        
    elif valinta == "3":
        print("Ohjelma loppu")
        break

    else:
        print("Lentoasemaa ei löydy.")