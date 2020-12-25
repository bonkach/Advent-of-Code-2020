from collections import *
from time import *
t1 = time()
ulaz = open('ulaz.txt', 'r')
sve = ulaz.read().strip()
ulaz.close()
trenutni = int(sve[0])
ll = dict()
for i in range(len(sve) - 1):
    ll[int(sve[i])] = int(sve[i + 1])
ll[int(sve[-1])] = 10
for i in range(10, 1000001):
    ll[i] = i + 1
ll[1000000] = trenutni
for i in range(10000000):
    prvi = ll[trenutni]
    drugi = ll[prvi]
    treći = ll[drugi]
    ll[trenutni] = ll[treći]
    destination = trenutni - 1
    if destination == 0:
        destination = 1000000
    while destination == prvi or destination == drugi or destination == treći:
        destination = destination - 1
        if destination < 1:
            destination = 1000000
    pokaz = ll[destination]
    ll[destination] = prvi
    ll[treći] = pokaz
    trenutni = ll[trenutni]
print(ll[1] * ll[ll[1]])
t2 = time()
print(t2 - t1)
