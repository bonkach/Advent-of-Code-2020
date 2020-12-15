from time import *
t1 = time()
ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
ulaz.close()
sve = sve.strip()
niz = sve.split(',')
rj = dict()
for i in range(len(niz) - 1):
    rj[niz[i]] = i
i = len(niz) - 1
uvjet = True
while len(niz) != 30000000:
    if niz[i] not in rj:
        niz.append('0')
        rj[niz[i]] = i
    else:
        razlika = i - rj[niz[i]]
        niz.append(str(razlika))
        rj[niz[i]] = i
    i += 1
print(niz[-1])
t2 = time()
print(t2 - t1)
