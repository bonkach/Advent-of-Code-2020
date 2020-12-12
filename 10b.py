ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
rj = dict()
for i in range(len(sve)):
    sve[i] = int(sve[i].strip())
    rj[sve[i]] = []
sve.sort()

for i in range(1, max(sve) + 1):
    if i in sve:
        if i + 1 in sve:
            rj[i].append(i + 1)
        if i + 2 in sve:
            rj[i].append(i + 2)
        if i + 3 in sve:
            rj[i].append(i + 3)
        rj[i].sort()
nepotrebni = 0
i = 2
while i< len(sve):
    if sve[i] - sve[i - 2] <= 3:
        nepotrebni += 1
    i += 1
print(2 ** nepotrebni)
