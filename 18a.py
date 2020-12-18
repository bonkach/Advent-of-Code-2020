ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
zbroj = 0
for red in sve:
    stog = []
    red = red.strip()
    znakovi = red.split()
    for znak in znakovi:
        if len(znak) > 1:
            if znak[0] == '(':
                for z in znak:
                    stog.append(z)
            else:
                if len(znak) == 3:
                    n = 2
                else:
                    n = 1
                for i in range(n):
                    operator = stog.pop()
                    while operator in '*+':
                        operand = stog.pop()
                        rezultat = znak[0] + operator + operand
                        stog.append(str(eval(rezultat)))
                        operator = stog.pop()
                    stog.pop()
                    if len(stog) > 0:
                        prije = stog.pop()
                        if prije in '*+':
                            još_prije = stog.pop()
                            rezultat = operator + prije + još_prije
                            stog.append(str(eval(rezultat)))
                        else:
                            stog.append(prije)
                            stog.append(operator)
                    else:
                        stog.append(operator)
        else:
            if znak not in '+*':
                if len(stog) == 0:
                    stog.append(znak)
                else:
                    operator = stog.pop()
                    operand = stog.pop()
                    rezultat = znak + operator + operand
                    stog.append(str(eval(rezultat)))
            else:
                stog.append(znak)
    zbroj += int(stog[0])
print(zbroj)
