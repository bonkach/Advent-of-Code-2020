ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
podaci = sve.split('\n\n')
brojač = 0
for zapis in podaci:
    if 'byr' in zapis and 'iyr' in zapis and\
       'eyr' in zapis and 'hgt' in zapis and\
       'hcl' in zapis and 'ecl' in zapis and\
       'pid' in zapis:
        polja = zapis.split()
        uvjet = True        
        for polje in polja:
            if polje[:3] == 'byr':
                dijelovi = polje.split(':')
                if int(dijelovi[1]) < 1920 or int(dijelovi[1]) > 2002:
                    uvjet = False
            if polje[:3] == 'iyr' and uvjet:
                dijelovi = polje.split(':')
                if int(dijelovi[1]) < 2010 or int(dijelovi[1]) > 2020:
                    uvjet = False
            if polje[:3] == 'eyr' and uvjet:
                dijelovi = polje.split(':')
                if int(dijelovi[1]) < 2020 or int(dijelovi[1]) > 2030:
                    uvjet = False
            if polje[:3] == 'hgt' and uvjet:
                dijelovi = polje.split(':')
                if dijelovi[1][-2:] != 'in' and dijelovi[1][-2:] != 'cm':
                    uvjet = False
                elif dijelovi[1][-2:] == 'in':
                    if int(dijelovi[1][:-2]) < 59 or int(dijelovi[1][:-2]) > 76:
                        uvjet = False
                else:
                    if int(dijelovi[1][:-2]) < 150 or int(dijelovi[1][:-2]) > 193:
                        uvjet = False
            if polje[:3] == 'hcl' and uvjet:
                dijelovi = polje.split(':')
                if dijelovi[1][0] != '#' or len(dijelovi[1]) != 7:
                    uvjet = False
                else:
                    for znak in dijelovi[1][1:]:
                        if znak not in '0123456789abcdef0':
                            uvjet = False
                            break
            if polje[:3] == 'ecl' and uvjet:
                dijelovi = polje.split(':')
                if dijelovi[1] != 'amb' and dijelovi[1] != 'blu' and \
                   dijelovi[1] != 'brn' and dijelovi[1] != 'gry' and \
                   dijelovi[1] != 'grn' and dijelovi[1] != 'hzl' and \
                   dijelovi[1] != 'oth':
                    uvjet = False
            if polje[:3] == 'pid' and uvjet:
                dijelovi = polje.split(':')
                if len(dijelovi[1]) != 9:
                    uvjet = False
                else:
                    for zn in dijelovi[1]:
                        if zn not in '0123456789':
                            uvjet = False
                            break
        if uvjet:
            brojač += 1
print(brojač)
ulaz.close()
