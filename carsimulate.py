def carsimulate(prog, xsize, zsize):
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
    x = xsize + xtotal
    y = zsize + ytotal
    print(x,y)

carsimulate("NWWWESNSNNSSEEWW", 100, 100)
