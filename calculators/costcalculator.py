def calculate(techid, level):
    '''Calculates the upgradecosts of a building.
Since OGame codes fleet and defensive structures as buildings,
upgrade costs of fleet and defensive structures are using the level
parameter as an amount parameter.

The "level" parameter calculates the price to upgrade TO the given level.'''

    #Costs can include Metal, Crystal, Deuterium and even Energy
    #The List encodes these costs in that order:
    #[Metal, Crystal, Deuterium, Energy]
    costs = [0, 0, 0, 0]

    #This monolith checks the techid and calculates the price

    #MetalMine
    if techid == 0 or techid == 1:
        costs[0] = int(40*1.5**level)
        costs[1] = int(15*1.5**level)

    #CrystalMine
    elif techid == 2:
        costs[0] = int(30*1.6**level)
        costs[1] = int(15*1.6**level)

    #DeuteriumSynthesizer
    elif techid == 3:
        costs[0] = int(150*1.5**level)
        costs[1] = int(50*1.5**level)

    #SolarPlant
    elif techid == 4:
        costs[0] = int(50*1.5**level)
        costs[1] = int(20*1.5**level)

    #FusionReactor
    elif techid == 12:
        costs[0] = int(500*1.8**level)
        costs[1] = int(200*1.8**level)
        costs[2] = int(100*1.8**level)

    #RoboticsFactory
    elif techid == 14:
        costs[0] = int(200*2**level)
        costs[1] = int(60*2**level)
        costs[2] = int(100*2**level)

    #NaniteFactory
    elif techid == 15:
        costs[0] = int(500000*2**level)
        costs[1] = int(250000*2**level)
        costs[2] = int(50000*2**level)

    #Shipyard
    elif techid == 21:
        costs[0] = int(200*2**level)
        costs[1] = int(100*2**level)
        costs[2] = int(50*2**level)

    #MetalStorage
    elif techid == 22:
        costs[0] = int(500*2**level)

    #CrystalStorage
    elif techid == 23:
        costs[0] = int(500*2**level)
        costs[1] = int(250*2**level)

    #DeuteriumTank
    elif techid == 24:
        costs[0] = int(500*2**level)
        costs[1] = int(500*2**level)

    print("Warning: Not fully implemented!")
    return costs
