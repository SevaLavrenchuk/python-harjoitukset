def karsi_parittomat(luvut):
    parilliset =[]

    for luku in luvut: 
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

#pääohjelma

testilista = [1,4,5,6,9]
karsittu_lista = karsi_parittomat(testilista)

print("Alkuperäinen lista: ", testilista)
print("Karsittu lista: ", karsittu_lista)