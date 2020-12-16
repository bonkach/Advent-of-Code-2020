ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
ulaz.close()
skup = set()
sve = sve.split('\n\n')
rj = dict()
for pravilo in sve[0].split('\n'):
    ime = pravilo[: pravilo.index(':')]
    skup = set()
    brojke = pravilo[pravilo.index(': ') + 1:]
    rangovi = brojke.split(' or ')
    for rang in rangovi:
        granice = rang.split('-')
        for i in range(int(granice[0]), int(granice[1]) + 1):
            skup |= {i}
    rj[ime] = skup
skup_sve = set()
for ključ in rj:
    skup_sve |= rj[ključ]
brojač = 0
karte = sve[2][sve[2].index('\n') + 1:]
karte = karte.split('\n')
mat = []
for red in karte:
    red = red.split(',')
    uvjet = True
    for karta in red:
        if int(karta) not in skup_sve:
            uvjet = False
    if uvjet:
        mat.append(red)
rj_konačno = dict()        
moja = sve[1].split('\n')[1].strip().split(',')
rj_imena = dict()
for k in range(len(mat[0])):
    rj_imena[k] = []
    skup_brojki = {int(moja[k])}
    for i in range(len(mat)):
        skup_brojki |= {int(mat[i][k])}
    for ključ in rj:
        if len(skup_brojki & rj[ključ]) == len(skup_brojki):
            rj_konačno[ključ] = moja[k]
            rj_imena[k].append(ključ)
bili = set()
for i in range(1, 21):
    for ključ in rj_imena:
        if len(rj_imena[ključ]) == i:
            for ime in rj_imena[ključ]:
                if ime not in bili:
                    rj_konačno[ime] = moja[ključ]
                    bili |= {ime}
umn = 1
for ključ in rj_konačno:
    if 'departure' in ključ:
        print(ključ)
        umn *= int(rj_konačno[ključ])
print(umn)
