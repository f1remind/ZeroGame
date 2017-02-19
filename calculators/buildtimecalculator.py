from calculators import costcalculator

def calculate(techid, level, robo, nani, shipyard, lab, technocrat=0):
    costs = costcalculator.calculate(techid, level)
    time = 0
    if not costs:
        print("[WARNING] Unknown techid:", techid)
    elif techid in range(100, 200): #Research techids
        time = (costs[0] + costs[1]) / (1000 * (1+lab))
        time *= 3600
        if technocrat:
            time *= 0.75
    elif techid >= 200: #Ships and defenses techids
        time = (costs[0] + costs[1]) / (2500 * (1 + shipyard) * 2**nani)
        time *= 3600
    else: 
        time = (costs[0] + costs[1]) * 0.5**nani * (1/(1+robo))
        time *= 1.44
        if techid not in [15, 41, 42, 43]:
            time /= max([4-(level/2), 1])

    return time
