def djelitelj(n, k):
    uvjet = True
    while n % k != 0:
        n -= 1
    return n

ulaz = open('ulaz.txt', 'r')
sve = ulaz.read().split('\n')
ulaz.close()
busevi = sve[1].split(',')
rj = dict()
for i in range(len(busevi)):
    if busevi[i] != 'x':
        rj[i] = int(busevi[i])     
najv = max(rj.values())
k = int(busevi[0])
uvjet = True
i = djelitelj(najv, k)
while uvjet:
    b = 0
    uvjet1 = True
    for ključ in rj:
        if (i + ključ) % rj[ključ] != 0:
            i = djelitelj(i + najv, k)
            uvjet1 = False
            break
    if uvjet1:
        uvjet = False
print(i)
    
            
