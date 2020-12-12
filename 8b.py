import copy
ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
rj = dict()
i = 0
l_zamj = []
for red in sve:
    red = red.strip()
    red = red.split()
    rj[i] = [red[0], red[1]]
    if red[0] == 'nop' or red[0] == 'jmp':
        l_zamj.append(i)
    i += 1
    
uvjet = True
k = 0
while uvjet and k < len(l_zamj):
    rj2 = copy.deepcopy(rj)
    if rj2[l_zamj[k]][0] == 'nop':
        rj2[l_zamj[k]][0] = 'jmp'
    else:
        rj2[l_zamj[k]][0] = 'nop'
    l_obiđenih = []
    i = 0
    acc = 0
    while i not in l_obiđenih:
        l_obiđenih.append(i)
        if rj2.get(i):
            naredba = rj2[i][0]
        else:
            uvjet = False
            break
        broj = int(rj2[i][1])
        if naredba == 'acc':
            acc += broj
            i += 1
        elif naredba == 'jmp':
            i += broj
        else:
             i += 1
    k += 1

print(acc)
