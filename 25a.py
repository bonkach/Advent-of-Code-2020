def loop_size(public_key):
    i = 1
    k = 0
    while i != public_key:
        i *= 7
        i %= 20201227
        k += 1
    return k

ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
card_public_key = int(sve[0])
door_public_key = int(sve[1])
card_loop_size = loop_size(card_public_key)
door_loop_size = loop_size(door_public_key)
i = 1
for k in range(door_loop_size):
    i *= card_public_key
    i %= 20201227
print(i)
