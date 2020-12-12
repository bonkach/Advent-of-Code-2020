ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
for i in range(len(sve)):
    sve[i] = int(sve[i].strip())
sve.sort()
j1 = 1
j2 = 0
j3 = 0
for i in range(1, max(sve) + 1):
    if i in sve:
        if i + 1 in sve:
            j1 += 1
        elif i + 2 in sve:
            j2 += 1
        else:
            j3 += 1
print(j1 * j3)
