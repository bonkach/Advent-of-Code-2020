ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
sve = sve.split('mask = ')
ulaz.close()
rj = dict()
for redovi in sve:
    redovi.strip()
    ins = redovi.split('\n')
    mask = ins[0]
    for instrukcija in ins[1:]:
        if instrukcija != '':
            red = instrukcija.split(' = ')
            mjesto = red[0][red[0].index('[') + 1:red[0].index(']')]
            kod = bin(int(red[1]))[2:]
            vrijednost = ''
            while len(kod) < 36:
                kod = '0' + kod
            for i in range(36):
                if mask[i] == 'X':
                    vrijednost += kod[i]
                else:
                    vrijednost += mask[i]
            rj[mjesto] = int(vrijednost, 2)
print(sum(rj.values()))
