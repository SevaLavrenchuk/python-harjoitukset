sanat = []
sama_sana = ""

while True: 
    sana = input("Anna sana lisättäväksi tarinaan:")
    if sana == "loppu":
        break
    if sana == sama_sana:
        break
    sanat.append(sana)
print(" ".join(sanat))