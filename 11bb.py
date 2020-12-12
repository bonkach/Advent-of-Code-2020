from time import *
t1 = time()
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
    n = 1
    uvjet = True
    for i in range(len(sve)):
        for j in range(len(red)):
            br_zauzetih = 0
            for susjed in susjedi:
                n = 1
                while (i + n * susjed[0] >= 0 and i + n * susjed[0] < len(sve)) and \
                      (j + n * susjed[1] >= 0 and j + n * susjed[1] < len(red)) and \
                      koo[(i + n * susjed[0], j + n * susjed[1])] == '.':
                    n += 1
                if (i + n * susjed[0] >= 0 and i + n * susjed[0] < len(sve)) and \
                      (j + n * susjed[1] >= 0 and j + n * susjed[1] < len(red)) and \
                      koo[(i + n * susjed[0], j + n * susjed[1])] == '#':
                    br_zauzetih += 1
            if koo[i, j] == 'L' and br_zauzetih == 0:
                koo1[i, j] = '#'
            elif koo[i, j] == '#' and br_zauzetih >= 5:
                koo1[i, j] = 'L'
##    for x in range(len(sve)):
##        for y in range(len(red)):
##            print(koo1[x, y], end = '')
##        print()
    if koo == koo1:
        promjena = True
    koo = copy.deepcopy(koo1)
broj = 0
for vr in koo.values():
    if vr == '#':
        broj += 1
print(broj)
t2 = time()
print(t2-t1)
