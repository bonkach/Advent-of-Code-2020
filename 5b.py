ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
l = []
sjedala = dict()
for zapis in sve:
    poč = 0; kraj = 127
    for red in zapis[:7]:
        if red == 'B':
            poč = poč + ((kraj - poč) // 2)
        elif red == 'F':
            kraj = poč + ((kraj - poč) // 2)
    p = 0; k = 7
    for st in zapis[7:]:
        if st == 'R':
            p = p + ((k - p) // 2)
        elif st == 'L':
            k = p + ((k - p) // 2)
    sjedala[kraj, k] = kraj * 8 + k
    l.append(kraj * 8 + k)
for x in range(128):
    for y in range(8):
        if (x, y) not in sjedala.keys():
            print(x, y)
