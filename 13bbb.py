ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
ulaz.close()
unos = sve.split(',')
rj = dict()
lista_indeksa = []
for i in range(len(unos)):
    if unos[i] != 'x':
        rj[i] = int(unos[i])
        lista_indeksa.append(i)
        
rj2 = dict()
for k in rj:
    b = (rj[k] - k) % rj[k]
    if b == rj[k]:
        b = 0
    rj2[rj[k]] = b
i = 0    
b = rj[lista_indeksa[i]]
a = rj2[b]
d = rj[lista_indeksa[i + 1]]
c = rj2[d]
for i in range(1, len(lista_indeksa) - 1):
    for x in range(a, b * d, b):
        if x % d == c:
            a = x
            b = b * d
            break
    d = rj[lista_indeksa[i + 1]]
    c = rj2[d]
for x in range(a, b * d, b):
        if x % d == c:
            a = x
            b = b * d
            break
print(x)
