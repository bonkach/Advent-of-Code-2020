from collections import *
ulaz = open('ulaz.txt', 'r')
sve = ulaz.read().strip()
ulaz.close()
cups = deque(sve)
for i in range(len(cups)):
    cups[i] = int(cups[i])
for i in range(100):
    pick_up1 = cups[1]
    pick_up2 = cups[2]
    pick_up3 = cups[3]
    for k in range(3):
        cups.remove(cups[1])
    destination = cups[0] - 1
    while destination not in cups:
        destination = destination - 1
        if destination < min(cups):
            destination = max(cups)
        
    mjesto = cups.index(destination)
    cups.insert(mjesto + 1, pick_up1)
    cups.insert(mjesto + 2, pick_up2)
    cups.insert(mjesto + 3, pick_up3)
    cups.append(cups.popleft())
while cups[0] != 1:
    cups.append(cups.popleft())
cups.popleft()
for broj in cups:
    print(broj, end = '')
