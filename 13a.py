ulaz = open('ulaz.txt', 'r')
sve = ulaz.read().split('\n')
ulaz.close()
vrijeme = int(sve[0])
busevi = dict()
for bus in sve[1].split(','):
    if bus != 'x':
        i = int(bus)
        k = i
        while k < vrijeme:
            k += i
        busevi[bus] = k - vrijeme
najmanji = min(busevi.values())
for ključ, vrijednost in busevi.items():
    if vrijednost == najmanji:
        print(int(ključ) * najmanji)
