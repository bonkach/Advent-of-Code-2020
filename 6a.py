ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
grupe = sve.split('\n\n')
brojač = 0
for grupa in grupe:
    grupa = grupa.replace('\n', '')
    skup = set(grupa)
    brojač += len(skup)
print(brojač)
ulaz.close()
