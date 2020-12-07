ulaz = open('ulaz.txt', 'r')
brojač = 0
sve = ulaz.readlines()
for red in sve:
    broj = 0
    pars = red.split()
    mjesto = pars[0].split('-')
    znak = pars[1][0]
    riječ = pars[2].strip()
    if znak == riječ[int(mjesto[0]) - 1]:
        broj += 1
    if znak == riječ[int(mjesto[1]) - 1]:
        broj += 1
    if broj == 1:
        brojač += 1
print(brojač)
