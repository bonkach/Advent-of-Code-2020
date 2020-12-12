from turtle import *
ulaz = open('ulaz.txt', 'r')
sve = ulaz.readlines()
ulaz.close()
for ins in sve:
    if ins[0] == 'N':
        goto(xcor(), ycor() + int(ins[1:]))
    elif ins[0] == 'S':
        goto(xcor(), ycor() - int(ins[1:]))
    elif ins[0] == 'W':
        goto(xcor() - int(ins[1:]), ycor())
    elif ins[0] == 'E':
        goto(xcor() + int(ins[1:]), ycor())
    elif ins[0] == 'L':
        lt(int(ins[1:]))
    elif ins[0] == 'R':
        rt(int(ins[1:]))
    else:
        fd(int(ins[1:]))
print(abs(xcor()) + abs(ycor()))
