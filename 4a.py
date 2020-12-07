ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
podaci = sve.split('\n\n')
brojač = 0
for zapis in podaci:
    if 'byr' in zapis and 'iyr' in zapis and\
       'eyr' in zapis and 'hgt' in zapis and\
       'hcl' in zapis and 'ecl' in zapis and\
       'pid' in zapis:
        brojač += 1
print(brojač)
ulaz.close()
