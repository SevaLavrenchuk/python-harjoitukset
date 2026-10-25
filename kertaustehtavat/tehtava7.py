sanat=["orava", "cappuchino", "talo", "aalto", "usko", "tietokone"]
yli_5_kirjainta = 0
for sana in sanat:
    if len(sana) > 5:
        yli_5_kirjainta+=1
print("Listan sanat: ", sanat)
print ("Sanat, joissa yli viisi kirjainta: ", yli_5_kirjainta ) 