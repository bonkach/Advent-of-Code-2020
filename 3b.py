def tobogan(i, sve, preskok):
    put = i
    brojač = 0
    if preskok == 0:
        korak = 1
    else:
        korak = preskok
    for j in range(preskok, len(sve), korak):
        red = sve[j].strip()
        red = list(red)
        while len(red) <= put:
            red += red
        if red[put] == '#':
            brojač += 1
            red[put] = 'X'
        else:
            red[put] = '0'
        put += i
    return brojač
umn = 1
for i in range(1,8,2):
    ulaz = open('ulaz.txt', 'r')
    sve = ulaz.readlines()
    umn *= tobogan(i, sve, 1)
    ulaz.close()
ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
umn *= tobogan(1, sve, 2)
ulaz.close()
print(umn)
