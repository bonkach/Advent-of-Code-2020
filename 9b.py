ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
uvjet = True
x = 0
y = 24
while uvjet:
    zbr = {}
    for i in range(x, y - 1):
        for j in range(i + 1, y + 1):
            zbr[(int(sve[i]), int(sve[j]))] = int(sve[i]) + int(sve[j])
    if int(sve[y + 1]) not in zbr.values():
        uvjet = False
        break
    x += 1
    y += 1

broj = sve[y + 1]
uvjet = True
x = 0
while uvjet:
    zbroj = 0
    i = x
    k = i
    l = []
    while zbroj <= int(sve[y + 1]):
        zbroj += int(sve[k])
        l.append(int(sve[k]))
        if zbroj == int(sve[y + 1]):
            print(min(l) + max(l))
            uvjet = False
            break
        k += 1
    x += 1
