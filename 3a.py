def tobogan(i, sve, preskok):
    put = i
    brojač = 0
    for j in range(preskok, len(sve)):
        red = sve[j].strip()
        while len(red) < put:
            red += red
        if red[put] == '#':
            brojač += 1
        put += i
    return brojač
umn = 1
for i in range(1,8,2):
    ulaz = open('ulaz.txt', 'r')
    sve = ulaz.readlines()[1:]
    umn *= tobogan(i, sve, 0)
    ulaz.close()
umn *= tobogan(i, sve, 2)
print(umn)
