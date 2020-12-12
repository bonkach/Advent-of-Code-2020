ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
l = []
for red in sve:
    red = red.strip()
    l.append(red)
l_obiđenih = []
i = 0
acc = 0
while i not in l_obiđenih:
    l_obiđenih.append(i)
    red = l[i].split()
    naredba = red[0]
    broj = int(red[1])
    if naredba == 'acc':
        acc += broj
        i += 1
    elif naredba == 'jmp':
        i += broj
    else:
         i += 1
print(acc)
    
