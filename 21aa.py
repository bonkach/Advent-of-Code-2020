# pritisnuti enter nakon inputa u tekstualnoj datoteci
ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
rj = dict()
rj_a = dict()
rj_s = dict()
for i in range(len(sve)):
    hrana = sve[i]
    dijelovi = hrana.split(' (')
    sastojci = dijelovi[0].split()
    alergeni = dijelovi[1][dijelovi[1].index(' ') + 1:-2].split(', ')
    rj_s[i] = set(sastojci)
    rj_a[i] = set(alergeni)
    for alergen in alergeni:
        if alergen not in rj:
            rj[alergen] = set(sastojci)
        else:
            rj[alergen] |= set(sastojci)
konačni = dict()
while len(rj) > 0:
    for k in rj_a:
        for alergen in rj_a[k]:
            if alergen in rj:
                rj[alergen] &= rj_s[k]
                for vr in konačni.values():
                    rj[alergen] -= vr
                if len(rj[alergen]) == 1:
                    konačni[alergen] = rj[alergen]
                    del(rj[alergen])
skup = set()
for k in konačni.values():
    skup |= k

broj = 0
for k in rj_s:
    broj += len(rj_s[k] - skup)
print(broj)
                 
        
                
    
