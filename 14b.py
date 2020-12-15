from time import *
t1 = time()
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
            mjesto = bin(int(red[0][red[0].index('[') + 1:red[0].index(']')]))[2:]
            kod = int(red[1])
            vrijednost = ''
            mjesto = mjesto.rjust(36, '0')
            l = []
            for i in range(36):
                if mask[i] == '0':
                    vrijednost += mjesto[i]
                elif mask[i] == '1':
                    vrijednost += '1'
                else:
                    vrijednost += 'X'
                    l.append(i)
            for i in range(2 ** len(l)):
                vr = list(vrijednost)
                konbi = bin(i)[2:]
                konbi = konbi.rjust(36, '0')
                for j in range(len(l)):
                    vr[l[j]] = konbi[j]
                vr = ''.join(vr)
                rj[int(vr, 2)] = kod
print(sum(rj.values()))
t2 = time()
print(t2 - t1)
