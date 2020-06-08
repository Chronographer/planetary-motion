from vpython import *
import numpy as np
import matplotlib.pyplot as plt
import positionVectorGenerator
import planetaryData


def run(planetObjectList, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, vPlot, numPlot, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    currentTime = 0.0

    planetSphereList = []
    for index in range(len(planetObjectList)):
        planetObject = planetObjectList[index]
        planetSphere = sphere(pos=planetObject.position, radius=sphereSizeList[index], color=color.green)
        planetSphereList.append(planetSphere)

    planetDistanceList = []  # list containing n lists, one for each planetObject. Each interior list contains the distance between itself and every other planet object
    for index in range(len(planetObjectList)):
        distanceToOtherPlanetObjectList = []
        planetDistanceList.append(distanceToOtherPlanetObjectList)

    planetForceList = []  # list containing n lists, one for each planetObject. Each interior list contains the force acting between itself and every other planet object
    for index in range(len(planetObjectList)):
        forceOnOtherPlanetObjectList = []
        planetForceList.append(forceOnOtherPlanetObjectList)

    planetAccelerationList = []  # list containing n lists, one for each planetObject. Each interior list contains the acceleration between itself and every other planet object
    for index in range(len(planetObjectList)):
        accelerationTowardsOtherPlanetObjectList = []
        planetAccelerationList.append(accelerationTowardsOtherPlanetObjectList)

    planetUnitVectorList = []
    for index in range(len(planetObjectList)):
        unitVectorList = []
        planetUnitVectorList.append(unitVectorList)

    planetAccelerationVectorList = []
    for index in range(len(planetObjectList)):
        accelerationVectorList = []
        planetAccelerationVectorList.append(accelerationVectorList)

    planetTotalAccelerationVectorList = []
    for index in range(len(planetObjectList)):
        planetTotalAccelerationVector = vector(0, 0, 0)
        planetTotalAccelerationVectorList.append(planetTotalAccelerationVector)

    if maxTrailLength != -2:
        for index in range(len(planetSphereList)):
            planetSphere = planetSphereList[index]
            planetSphere.trail = curve(pos=planetSphere.pos, color=color.red, radius=trailRadius, retain=maxTrailLength, interval=30)
    gravitationalConstant = (4 * np.pi ** 2) / planetaryData.sunMass

    while currentTime < endTime:
        for index in range(len(planetObjectList)):  # computes the distance between each planet object and every other planet object, avoiding duplication.
            currentPlanetObject = planetObjectList[index]
            currentPlanetDistanceList = planetDistanceList[index]
            currentPlanetDistanceList.clear()
            for innerIndex in range(len(planetObjectList)):  # starts at index so that it doesnt duplicate any distances.
                comparisonPlanetObject = planetObjectList[innerIndex]
                if innerIndex != index:
                    distance = np.sqrt((currentPlanetObject.position.x - comparisonPlanetObject.position.x) ** 2 + (currentPlanetObject.position.y - comparisonPlanetObject.position.y) ** 2 + (currentPlanetObject.position.z - comparisonPlanetObject.position.z) ** 2)
                    currentPlanetDistanceList.append(distance)
                else:  # make the distance between a planetObject and itself something that cannot possibly be accidentally used in a mathematical operation.
                    distance = "self"
                    currentPlanetDistanceList.append(distance)
            planetDistanceList[index] = currentPlanetDistanceList

        for index in range(len(planetObjectList)):  # computes the force between each planet object and every other planet object, avoiding duplication.
            currentPlanetObject = planetObjectList[index]
            currentPlanetForceList = planetForceList[index]
            currentPlanetDistanceList = planetDistanceList[index]
            currentPlanetForceList.clear()
            for innerIndex in range(len(currentPlanetDistanceList)):  # starts at index so that it doesnt duplicate any forces.
                comparisonPlanetObject = planetObjectList[innerIndex]
                comparisonPlanetDistance = currentPlanetDistanceList[innerIndex]
                if innerIndex != index:
                    force = (gravitationalConstant * currentPlanetObject.mass * comparisonPlanetObject.mass) / (comparisonPlanetDistance ** 2)
                    currentPlanetForceList.append(force)
                else:  # make the force acting on a planetObject and itself something that cannot possibly be accidentally used in a mathematical operation.
                    force = "self"
                    currentPlanetForceList.append(force)
            planetForceList[index] = currentPlanetForceList

        for index in range(len(planetObjectList)):  # computes the acceleration felt between each planetObject and every other planetObject. Note: This is consistent with threeBodyProblem.py and works correctly. (for the first timestep at least)
            currentPlanetObject = planetObjectList[index]
            currentPlanetForceList = planetForceList[index]
            currentPlanetAccelerationList = planetAccelerationList[index]
            currentPlanetAccelerationList.clear()
            for innerIndex in range(len(currentPlanetForceList)):
                comparisonPlanetForce = currentPlanetForceList[innerIndex]
                if comparisonPlanetForce != "self":
                    acceleration = comparisonPlanetForce / currentPlanetObject.mass
                    currentPlanetAccelerationList.append(acceleration)
                else:  # make the acceleration of one planetObject towards itself something that cannot possibly be accidentally used in a mathematical operation.
                    acceleration = "self"
                    currentPlanetAccelerationList.append(acceleration)
            planetAccelerationList[index] = currentPlanetAccelerationList

        for index in range(len(planetObjectList)):  # computes the acceleration vector between each planet object and every other planetObject. Note: I combined the chunk that computes the unit position vector and the following chunk which computes the acceleration vectors into this single chunk.
            currentPlanetObject = planetObjectList[index]  # Note: This chunk appears to be working correctly and matches what I see in threeBodyProblem.py (for the first timestep at least)
            # currentPlanetUnitPositionVectorList = planetUnitVectorList[index]
            currentPlanetAccelerationList = planetAccelerationList[index]
            currentPlanetAccelerationVectorList = planetAccelerationVectorList[index]
            currentPlanetAccelerationVectorList.clear()
            for innerIndex in range(len(planetObjectList)):
                if innerIndex != index:
                    comparisonPlanetObject = planetObjectList[innerIndex]
                    comparisonPlanetAcceleration = currentPlanetAccelerationList[innerIndex]
                    unitPositionVector = norm(positionVectorGenerator.generatePositionVector(currentPlanetObject, comparisonPlanetObject))
                    if comparisonPlanetAcceleration != "self":
                        accelerationVector = unitPositionVector * comparisonPlanetAcceleration
                        currentPlanetAccelerationVectorList.append(accelerationVector)
                    else:
                        accelerationVector = "self"
                        currentPlanetAccelerationVectorList.append(accelerationVector)
                    # currentPlanetUnitPositionVectorList.append(unitPositionVector)
                else:  # make the acceleration vector between a planetObject and itself something that cannot possibly be accidentally used in a mathematical operation.
                    # unitPositionVector = "self"
                    # currentPlanetUnitPositionVectorList.append(unitPositionVector)
                    accelerationVector = "self"
                    currentPlanetAccelerationVectorList.append(accelerationVector)
            # planetUnitVectorList[index] = currentPlanetUnitPositionVectorList
            planetAccelerationVectorList[index] = currentPlanetAccelerationVectorList

        for index in range(len(planetObjectList)):  # adds all acceleration vectors associated with each planetObject together. NOTE: This works as expected for the first frame at least.
            currentPlanetAccelerationVectorList = planetAccelerationVectorList[index]
            currentPlanetTotalAccelerationVector = planetTotalAccelerationVectorList[index]
            for innerIndex in range(len(currentPlanetAccelerationVectorList)):
                if innerIndex != index:
                    comparisonPlanetAccelerationVector = currentPlanetAccelerationVectorList[innerIndex]
                    currentPlanetTotalAccelerationVector = currentPlanetTotalAccelerationVector + comparisonPlanetAccelerationVector
            planetTotalAccelerationVectorList[index] = currentPlanetTotalAccelerationVector

        for index in range(len(planetObjectList)):  # computes the new position and velocity of each planet object Note: This works for earth for at least the first frame.
            currentPlanetTotalAccelerationVector = planetTotalAccelerationVectorList[index]
            currentPlanetObject = planetObjectList[index]
            currentPlanetObject.velocity = currentPlanetObject.velocity + (currentPlanetTotalAccelerationVector * timeStep)
            currentPlanetObject.position = currentPlanetObject.position + (currentPlanetObject.velocity * timeStep)

        currentTime = currentTime + timeStep

        for index in range(len(planetSphereList)):  # updates the graphical position of each of the planetObjects.
            currentPlanetSphere = planetSphereList[index]
            currentPlanetObject = planetObjectList[index]
            currentPlanetSphere.pos = currentPlanetObject.position

        if maxTrailLength != -2:  # if trails are enabled, add a new segment to the trails of each of the planet spheres.
            for index in range(len(planetSphereList)):
                currentPlanetSphere = planetSphereList[index]
                currentPlanetSphere.trail.append(currentPlanetSphere.pos)

        rate(targetFrameRate)
