ulaz = open('ulaz.txt', 'r')
import copy
sve = ulaz.readlines()
ulaz.close()
j = 0
koo = dict()
for i in range(len(sve)):
    red = sve[i].strip()
    for j in range(len(red)):
        koo[i, j] = red[j]
promjena = False
susjedi = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
while not promjena:
    koo1 = copy.deepcopy(koo)
    for i in range(len(sve)):
        for j in range(len(red)):
            br_praznih = 0
            br_zauzetih = 0
            br_pod = 0
            for susjed in susjedi:
                if koo.get((i + susjed[0], j + susjed[1]), 'L') == 'L':
                    br_praznih += 1
                elif koo.get((i + susjed[0], j + susjed[1]), 'L') == '#':
                    br_zauzetih += 1
                else:
                    br_pod += 1
            if koo[i, j] == 'L' and br_praznih + br_pod == 8:
                koo1[i, j] = '#'
            elif koo[i, j] == '#' and br_zauzetih >= 4:
                koo1[i, j] = 'L'
    if koo == koo1:
        promjena = True
    koo = copy.deepcopy(koo1)
broj = 0
for vr in koo.values():
    if vr == '#':
        broj += 1
print(broj)
