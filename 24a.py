ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
koo = dict()
for red in sve:
    x = y = z = 0
    i = 0
    red = red.strip()
    while i < len(red):
        if red[i] == 's':
            if red[i + 1] == 'e':
                z += 1
                y -= 1
                i += 2
            else:
                x -= 1
                z += 1
                i += 2
        elif red[i] == 'n':
            if  red[i + 1] == 'e':
                x += 1
                z -= 1
                i += 2
            else:
                y += 1
                z -= 1
                i += 2
        elif red[i] == 'w':
            x -= 1
            y += 1
            i += 1
        else:
            x += 1
            y -= 1
            i += 1
    if (x, y, z) not in koo:
        koo[(x, y, z)] = 1
    else:
        koo[(x, y, z)] = 0
b = 0
for vr in koo.values():
    if vr:
        b += 1
print(b)
