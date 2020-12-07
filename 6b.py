ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
grupe = sve.split('\n\n')
brojač = 0
for grupa in grupe:
    članovi = grupa.split('\n')
    presjek = set(članovi[0])
    for član in članovi:
        presjek &= set(član)
    brojač += len(presjek)
print(brojač)
ulaz.close()
