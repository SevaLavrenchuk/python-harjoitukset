hedelmat = {"ananas" : 12,
            "sitruuna" : 5,
            "omena" : 3}

hedelma = input("Anna hedelmän nimi: (ananas, sitruuna tai omena)")
if hedelma in hedelmat: 
    print (f"Hedelmäsi hinta on: {hedelmat[hedelma]}e.")
else:
    print ("Tuote ei löydy valikoimasta.")