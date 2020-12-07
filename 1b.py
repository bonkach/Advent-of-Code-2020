ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
for i in range(len(sve) - 2):
    for j in range(i, len(sve) - 1):
        for k in range(j, len(sve)):
            if int(sve[i]) + int(sve[j]) + int(sve[k]) == 2020:
                print(int(sve[i]) * int(sve[j]) * int(sve[k]))
                break
