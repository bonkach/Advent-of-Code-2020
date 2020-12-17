import copy
ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
rj = dict()
for i in range(len(sve)):
    red = sve[i].strip()
    for j in range(len(red)):
        rj[(i, j, 0)] = sve[i][j]
susjedi = []
for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            susjedi.append((i, j, k))
susjedi.pop(susjedi.index((0,0,0)))  
rj2 = copy.deepcopy(rj)
for k in rj:
    for s in susjedi:
        if rj.get((k[0] + s[0], k[1] + s[1], k[2] + s[2]), '.') == '.':
            rj2[k[0] + s[0], k[1] + s[1], k[2] + s[2]] = '.'
rj = copy.deepcopy(rj2)
for i in range(6):
    for k in rj:
        br_aktivnih_suseda_ćo = 0
        for s in susjedi:
            if rj.get((k[0] + s[0], k[1] + s[1], k[2] + s[2]), '.') == '#':
                br_aktivnih_suseda_ćo += 1
        if rj[k] == '#' and br_aktivnih_suseda_ćo != 2 and br_aktivnih_suseda_ćo != 3:
            rj2[k] = '.'
        if rj[k] == '.' and br_aktivnih_suseda_ćo == 3:
            rj2[k] = '#'
    rj = copy.deepcopy(rj2)
    for k in rj:
        for s in susjedi:
            if rj.get((k[0] + s[0], k[1] + s[1], k[2] + s[2]), '.') == '.':
                rj2[k[0] + s[0], k[1] + s[1], k[2] + s[2]] = '.'
    rj = copy.deepcopy(rj2)
brojač = 0
for k in rj:
    if rj[k] == '#':
        brojač += 1
print(brojač)
