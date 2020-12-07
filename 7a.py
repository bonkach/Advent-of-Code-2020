ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
rj = dict()
brojač = 0
indirektni = set()
direktni = set()
for pravilo in sve:
    riječi = pravilo.split('contain')
    l = riječi[0][:riječi[0].index(' bags')]
    d = riječi[1].split(',')
    rj[l] = []
    for član in d:
        član = član.strip()
        broj = član[0]
        boja = član[2:član.index(' bag')]
        rj[l].append((boja, broj))
        if boja == 'shiny gold':
            direktni |= {l}
uvjet = True
while uvjet:
    uvjet = False
    for ključ, vrijednost in rj.items():
        for boja, broj in vrijednost:
            if boja in direktni:
                direktni |= {ključ}
                uvjet = True
print(len(direktni))

