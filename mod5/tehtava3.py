luku = int(input("Anna kokonaisluku:"))
alkuluku = True
if luku < 2:
   alkuluku = False
else: 
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            alkuluku = False
if alkuluku:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")