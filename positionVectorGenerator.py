from vpython import vector


def generatePositionVector(planetOne, planetTwo):
    differenceX = planetTwo.position.x - planetOne.position.x
    differenceY = planetTwo.position.y - planetOne.position.y
    differenceZ = planetTwo.position.z - planetOne.position.z
    positionVector = vector(differenceX, differenceY, differenceZ)
    return positionVector
