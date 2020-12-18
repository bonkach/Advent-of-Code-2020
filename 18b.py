ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
zbroj = 0
for red in sve:
    red = red.strip()
    while ')' in red:
        k = red.index(')')
        p = k
        while red[p] != '(':
            p -= 1
        stari_deo = red[p + 1:k]
        deo = stari_deo[:]
        while '+' in deo:
            i = deo.index('+')
            pp = i - 2
            kk = i + 2
            while deo[kk] == ' ':
                kk += 1
            while pp > 0 and deo[pp] in '1234567890':
                pp -= 1
            while kk < len(deo) and deo[kk] in '1234567890':
                kk += 1
            d = deo[pp: kk + 1]
            reza = eval(d)
            deo = deo.replace(d, ' ' + str(reza) + ' ')
        red = red.replace('(' + stari_deo + ')', str(eval(deo)))
    while '+' in red:
        i = red.index('+')
        pp = i - 2
        kk = i + 2
        while pp > 0 and red[pp] in '1234567890':
            pp -= 1
        while kk < len(red) and red[kk] in '1234567890':
            kk += 1
        d = red[pp: kk + 1]
        reza = eval(d)
        red = red.replace(d, ' ' + str(reza) + ' ')
    z = eval(red)
    zbroj += z
print(zbroj)
