from turtle import *
ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
tracer(False)
wp = [10, 1]
for ins in sve:
    if ins[0] == 'N':
        wp[1] += int(ins[1:])
    elif ins[0] == 'S':
        wp[1] -= int(ins[1:])
    elif ins[0] == 'W':
        wp[0] -= int(ins[1:])
    elif ins[0] == 'E':
        wp[0] += int(ins[1:])
    elif ins[0] == 'L':
        a = wp[0]; b = wp[1]
        if int(ins[1:]) == 90:
            wp[0], wp[1] = -b, a
        elif int(ins[1:]) == 180:
            wp[0], wp[1] = -a, -b
        else:
            wp[0], wp[1] = b, -a
    elif ins[0] == 'R':
        a = wp[0]; b = wp[1]
        if int(ins[1:]) == 90:
            wp[0], wp[1] = b, -a
        elif int(ins[1:]) == 180:
            wp[0], wp[1] = -a, -b
        else:
            wp[0], wp[1] = -b, a
    else:
        goto(xcor() + (wp[0] * int(ins[1:])), ycor() + (wp[1] * int(ins[1:])))
print(abs(xcor()) + abs(ycor()))
tracer(True)
