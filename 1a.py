ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
for i in range(len(sve) - 1):
    for j in range(i, len(sve)):
        if int(sve[i]) + int(sve[j]) == 2020:
            print(int(sve[i]) * int(sve[j]))
            break
