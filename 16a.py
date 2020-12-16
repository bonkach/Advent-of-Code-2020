ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
ulaz.close()
skup = set()
sve = sve.split('\n\n')
for pravilo in sve[0].split('\n'):
    brojke = pravilo[pravilo.index(': ') + 1:]
    rangovi = brojke.split(' or ')
    for rang in rangovi:
        granice = rang.split('-')
        for i in range(int(granice[0]), int(granice[1]) + 1):
            skup |= {i}
brojač = 0
karte = sve[2][sve[2].index('\n') + 1:]
karte = karte.split('\n')
for red in karte:
    red = red.split(',')
    for karta in red:
        if int(karta) not in skup:
            brojač += int(karta)
print(brojač)
    
