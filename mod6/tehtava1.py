import random

def heita_noppa():
    return random.randint (1,6)
silmäluku = 0

while silmäluku != 6:
    silmäluku = heita_noppa ()
    print(silmäluku)