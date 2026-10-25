tuotteet = []
maarat = []

while True: 
    tuote = input("Mitä tuotetta valmistetaan?")
    maara = int(input("Kuinka monta?"))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatko = input("Jatketaanko tuotantoa? ")
    if jatko.lower() != "kyllä":
        break

print("Tuotanto lopetettu. Valmistetut tuotteet: ")

for i in range(len(tuotteet)):
        print(f"{tuotteet[i]}: {maarat[i]} kpl")
        