def calculate(techid, level, plasma=0, energy=1, item=1, geologist=False):
    prod = [0, 0, 0, 0]
    if techid == 1 or techid == 0:
        prod[0] = 30*level*1.1**level * energy * item
        if geologist:
            prod[0] *= 1.1
        prod[0] = int(prod[0]) * ((100 + 1 * plasma)/100) / 3600
        prod[0] += 30
    elif techid == 2:
        prod[1] = 20*level*1.1**level*energy*item
        if geologist:
            prod[1] *= 1.1
        prod[1] = int(prod[1])*((100+(2/3)*plasma)/100) / 3600
        prod[1] += 15

    return prod
