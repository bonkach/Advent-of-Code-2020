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
        print(sve[y + 1])
        uvjet = False
    x += 1
    y += 1
        
