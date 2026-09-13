sukupuoli = input("Mikä on sinun biologinen sukupuoli? (mies/nainen)")
hemoglobiiniarvo = int(input("Mikä on sinun hemoglobiiniarvo? (g/l)"))
if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvosi on korkea")
    else:
        print("Hemoglobiiniarvosi on normaali")

elif sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvosi on matala")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvosi on korkea")
    else:
        print("Hemoglobiiniarvosi on normaali")


