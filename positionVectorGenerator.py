from vpython import vector


def generatePositionVector(planetOne, planetTwo):
    positionVector = planetTwo.position - planetOne.position
    """differenceX = planetTwo.position.x - planetOne.position.x
    differenceY = planetTwo.position.y - planetOne.position.y
    differenceZ = planetTwo.position.z - planetOne.position.z
    positionVector = vector(differenceX, differenceY, differenceZ)""" # I originally did this because I could not get it to correctly subtract vectors, and I now realized that I was subtracting them in the wrong order, so this whole class is probably no longer necessary. (4-15-2015)
    return positionVector
