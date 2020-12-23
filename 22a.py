from collections import deque
ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
ulaz.close()
igrači = sve.split('\n\n')
prvi = deque(igrači[0].split('\n')[1:])
drugi = deque(igrači[1].split('\n')[1:])
while len(prvi) != 0 and len(drugi) != 0:
    a = int(prvi.popleft())
    b = int(drugi.popleft())
    if a > b:
        prvi.extend([str(a), str(b)])
    else:
        drugi.extend([str(b), str(a)])
if len(prvi) > 0:
    l = prvi
else:
    l = drugi
l.reverse()
rezultat = 0
for i in range(len(l)):
    rezultat += int(l[i]) * (i + 1)
print(rezultat)
    
