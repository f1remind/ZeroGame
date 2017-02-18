def calculate(techid, level):
    '''Calculates the upgradecosts of a building.
Since OGame codes fleet and defensive structures as buildings,
upgrade costs of fleet and defensive structures are using the level
parameter as an amount parameter.

The "level" parameter calculates the price to upgrade TO the given level.'''

    #The level should be an integer
    level = int(level)

    #Costs can include Metal, Crystal, Deuterium and even Energy
    #The List encodes these costs in that order:
    #[Metal, Crystal, Deuterium, Energy]
    costs = [0, 0, 0, 0]

    #This monolith checks the techid and calculates the price

    #MetalMine
    if techid == 0 or techid == 1:
        costs[0] = int(40*1.5**level)
        costs[1] = int(10*1.5**level)

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

    #MetalDen (Legacy)
    elif techid == 25:
        costs[0] = int(1150*2.3**level)

    #CrystalDen (Legacy)
    elif techid == 26:
        costs[0] = int(1150*2.3**level)
        costs[1] = int(575*2.3**level)

    #DeuteriumDen (Legacy)
    elif techid == 27:
        costs[0] = int(1150*2.3**level)
        costs[1] = int(1150*2.3**level)

    #ResearchLab
    elif techid == 31:
        costs[0] = int(100*2**level)
        costs[1] = int(200*2**level)
        costs[2] = int(100*2**level)

    #Terraformer
    elif techid == 33:
        costs[1] = int(25000*2**level)
        costs[2] = int(50000*2**level)
        costs[3] = int(500*2**level)

    #AllianceDepot
    elif techid == 34:
        costs[0] = int(10000*2**level)
        costs[1] = int(20000*2**level)

    #SpaceDock
    elif techid == 36:
        costs[0] = int(40*5**level)
        costs[2] = int(10*5**level)
        costs[3] = int(10*5**level)

    #LunarBase
    elif techid == 41:
        costs[0] = int(10000*2**level)
        costs[1] = int(20000*2**level)
        costs[2] = int(10000*2**level)

    #SensorPhalanx
    elif techid == 42:
        costs[0] = int(10000*2**level)
        costs[1] = int(20000*2**level)
        costs[2] = int(10000*2**level)

    #JumpGate
    elif techid == 43:
        costs[0] = int(1000000*2**level)
        costs[1] = int(2000000*2**level)
        costs[2] = int(1000000*2**level)

    #MissileSilo
    elif techid == 44:
        costs[0] = int(10000*2**level)
        costs[1] = int(10000*2**level)
        costs[2] = int(500*2**level)

    #EspionageTechnology
    elif techid == 106:
        costs[0] = int(100*2**level)
        costs[1] = int(500*2**level)
        costs[2] = int(100*2**level)

    #ComputerTechnology
    elif techid == 108:
        costs[1] = int(200*2**level)
        costs[2] = int(300*2**level)

    #WeapenTechnology
    elif techid == 109:
        costs[0] = int(400*2**level)
        costs[1] = int(100*2**level)

    #Shielding Technology
    elif techid == 110:
        costs[0] = int(100*2**level)
        costs[1] = int(300*2**level)

    #ArmorTechnology
    elif techid == 111:
        costs[0] = int(500*2**level)

    #EnergyTechnology
    elif techid == 113:
        costs[1] = int(400*2**level)
        costs[2] = int(200*2**level)

    #HyperspaceTechnology
    elif techid == 114:
        costs[1] = int(2000*2**level)
        costs[2] = int(1000*2**level)

    #CombustionDrive
    elif techid == 115:
        costs[0] = int(200*2**level)
        costs[2] = int(300*2**level)

    #ImpulseDrive
    elif techid == 117:
        costs[0] = int(1000*2**level)
        costs[1] = int(2000*2**level)
        costs[2] = int(300*2**level)

    #HyperspaceDrive
    elif techid == 118:
        costs[0] = int(5000*2**level)
        costs[1] = int(10000*2**level)
        costs[2] = int(3000*2**level)

    #LaserTechnology
    elif techid == 120:
        costs[0] = int(100*2**level)
        costs[1] = int(50*2**level)

    #IonTechnology
    elif techid == 121:
        costs[0] = int(500*2**level)
        costs[1] = int(150*2**level)
        costs[2] = int(50*2**level)

    #PlasmaTechnology
    elif techid == 122:
        costs[0] = int(1000*2**level)
        costs[1] = int(2000*2**level)
        costs[2] = int(500*2**level)

    #InterplanetaryResearchNetwork
    elif techid == 123:
        costs[0] = int(120000*2**level)
        costs[1] = int(200000*2**level)
        costs[2] = int(80000*2**level)

    #Astrophysics
    elif techid == 124:
        costs[0] = 100*int(0.5 + 40*1.75**(level-1))
        costs[1] = 100*int(0.5 + 80*1.75**(level-1))
        costs[2] = 100*int(0.5 + 40*1.75**(level-1))

    #GravitonTechnology
    elif techid == 199:
        costs[3] = int(100000*3**level)

    #SmallCargoShip
    elif techid == 202:
        costs[0] = 2000*level
        costs[1] = 2000*level

    #LargeCargoship
    elif techid == 203:
        costs[0] = 6000*level
        costs[1] = 6000*level

    #LightFighter
    elif techid == 204:
        costs[0] = 3000*level
        costs[1] = 1000*level

    #HeavyFighter
    elif techid == 205:
        costs[0] = 6000*level
        costs[1] = 4000*level

    #Cruiser
    elif techid == 206:
        costs[0] = 20000*level
        costs[1] = 7000*level
        costs[2] = 2000*level

    #Battleship
    elif techid == 207:
        costs[0] = 45000*level
        costs[1] = 15000*level

    #ColonyShip
    elif techid == 208:
        costs[0] = 10000*level
        costs[1] = 20000*level
        costs[2] = 10000*level

    #Recycler
    elif techid == 209:
        costs[0] = 10000*level
        costs[1] = 6000*level
        costs[2] = 2000*level

    #EspionageProbe
    elif techid == 210:
        costs[1] = 1000*level

    #Bomber
    elif techid == 211:
        costs[0] = 50000*level
        costs[1] = 25000*level
        costs[2] = 15000*level

    #SolarSatellite
    elif techid == 212:
        costs[1] = 2000*level
        costs[2] = 500*level

    #Destroyer
    elif techid == 213:
        costs[0] = 60000*level
        costs[1] = 50000*level
        costs[2] = 15000*level

    #Deathstar
    elif techid == 214:
        costs[0] = 5000000*level
        costs[1] = 4000000*level
        costs[2] = 1000000*level

    #Battlecruiser
    elif techid == 215:
        costs[0] = 30000*level
        costs[1] = 40000*level
        costs[2] = 15000*level

    #RocketLauncher
    elif techid == 401:
        costs[0] = 2000*level

    #LightLaser
    elif techid == 402:
        costs[0] = 1500*level
        costs[1] = 500*level

    #HeavyLaser
    elif techid == 403:
        costs[0] = 6000*level
        costs[1] = 2000*level

    #GaussCannon
    elif techid == 404:
        costs[0] = 20000*level
        costs[1] = 15000*level
        costs[2] = 2000*level

    #IonCannon
    elif techid == 405:
        costs[0] = 2000*level
        costs[1] = 6000*level

    #PlasmaTurret
    elif techid == 406:
        costs[0] = 50000*level
        costs[1] = 50000*level
        costs[2] = 30000*level

    #SmallShieldDome
    elif techid == 407:
        costs[0] = 10000*level  
        costs[1] = 10000*level

    #LargeShieldDome
    elif techid == 408:
        costs[0] = 50000*level
        costs[1] = 50000*level

    #AntiBallisticMissile
    elif techid == 502:
        costs[0] = 8000*level
        costs[2] = 2000*level

    #InterplanetaryMissile
    elif techid == 503:
        costs[0] = 12500*level
        costs[1] = 2500*level
        costs[2] = 10000*level

    else: print("[WARNING] Unknown techid:", techid)

    return costs
