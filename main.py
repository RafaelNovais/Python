def snooker(n):
    t = 0
    for i in range(0, n + 1):
        t += i
        t
    print(t)


snooker(12)


def mySum(x, y):
    return x + y


def mySub(x, y):
    return x - y


print(mySum(2, 7))
print(mySub(8, 10))

import math


def simulate(prog, xsize, zsize):
    xtotal = 0
    ytotal = 0

    for i in prog:
        if i == "N":
            xtotal += 1
        elif i == "S":
            xtotal -= 1
        elif i == "E":
            ytotal -= 1
        elif i == "W":
            ytotal += 1
        print(i)
        print(xtotal)
        print(ytotal)

    x = xsize + xtotal
    y = zsize + ytotal
    print(x)
    print(y)


simulate("NNNSSEEWW", 100, 100)
