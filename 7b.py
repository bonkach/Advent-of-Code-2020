ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
rj = dict()
ulaz.close()
for pravilo in sve:
    riječi = pravilo.split('contain')
    l = riječi[0][:riječi[0].index(' bags')]
    d = riječi[1].split(',')
    rj[l] = []
    for član in d:
        član = član.strip()
        if član[0] != 'n':
            broj = član[0]
        else:
            broj = '0'
        boja = član[2:član.index(' bag')]
        rj[l].append((boja, broj))

zbrojevi = dict()
for el in rj:
    z = 0
    for e in rj[el]:
        z += int(e[1])
    zbrojevi[el] = z
    
prošli = ['shiny gold']
zbroj = 0
while len(prošli) > 0:
    ključ = prošli.pop()
    zbroj += zbrojevi[ključ]
    for boja, broj in rj[ključ]:
        if boja != ' other':
            for i in range(int(broj)):
                prošli.append(boja)
print(zbroj)
            
        
    
        
