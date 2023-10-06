def main():
    intMass = int(input("m: "))
    print(getEnergy(intMass))

def getEnergy(mass):
    speed = 300000000
    return mass * pow(speed,2)

main()