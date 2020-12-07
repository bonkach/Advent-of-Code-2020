ulaz = open('ulaz.txt', 'r')
brojač = 0
sve = ulaz.readlines()
for red in sve:
    pars = red.split()
    količina = pars[0].split('-')
    znak = pars[1][0]
    riječ = pars[2].strip()
    broj = riječ.count(znak)
    if int(količina[0]) <= broj <= int(količina[1]):
        brojač += 1
print(brojač)
