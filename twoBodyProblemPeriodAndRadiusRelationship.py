from vpython import *
import numpy as np
import matplotlib.pyplot as plt
import positionVectorGenerator

""" This program simulates a simple 2-body system. Note that it assumes the effects of the first planet object ("planet") 
on the second planet object ("sun") are so small as to be negligable, so position, velocity, ect, are only computed for 
the "planet" object. Note however that any planet object may be used in place of "planet". """


def run(planet, sun, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    sunSphere = sphere(pos=vector(0, 0, 0), radius=sphereSizeList[1], color=color.yellow)
    planetSphere = sphere(pos=planet.position, radius=sphereSizeList[0], texture=textures.earth, shininess=0)

    gravitationalConstant = (4 * np.pi ** 2) / sun.mass
    currentTime = 0
    currentPeriodStartTime = currentTime
    singlePeriodTimeList = []
    averagePeriodTimeList = []
    timeList = []
    plotList = []
    periodSquaredList = []
    radiusCubedList = []

    multiplePeriodTime = 0

    orbitRadiusListPopulator = 1
    maxOrbitRadius = 30
    orbitRadiusIncrement = 1
    planetOrbitRadiiList = []

    while orbitRadiusListPopulator <= maxOrbitRadius:
        planetOrbitRadiiList.append(orbitRadiusListPopulator)
        orbitRadiusListPopulator = orbitRadiusListPopulator + orbitRadiusIncrement

    if maxTrailLength != -2:
        planetSphere.trail = curve(pos=[planetSphere.pos], color=color.white, radius=trailRadius, retain=maxTrailLength, interval=30)

    for index in range(len(planetOrbitRadiiList)):
        currentRadius = planetOrbitRadiiList[index]
        initialVelocity = np.sqrt((4 * pi ** 2) / currentRadius)
        planet.velocity = vector(vector(0, initialVelocity, 0))
        planet.position = vector(currentRadius, 0, 0)
        currentPeriodStartTime = currentTime

        while len(singlePeriodTimeList) < endTime:
            lastXVelocity = planet.velocity.x
            distancePlanetSun = np.sqrt((planet.position.x ** 2 + planet.position.y ** 2 + planet.position.z ** 2))
            forcePlanetSun = (gravitationalConstant * planet.mass * sun.mass) / (distancePlanetSun ** 2)
            accelerationPlanetSun = forcePlanetSun / planet.mass
            unitPositionVectorPlanetSun = norm(positionVectorGenerator.generatePositionVector(planet, sun))
            accelerationVectorPlanetSun = accelerationPlanetSun * unitPositionVectorPlanetSun
            accelerationVectorPlanet = accelerationVectorPlanetSun
            planet.velocity = planet.velocity + (accelerationVectorPlanet * timeStep)
            planet.position = planet.position + (planet.velocity * timeStep)
            planetSphere.pos = planet.position
            currentTime = currentTime + timeStep
            rate(targetFrameRate)

            if lastXVelocity > 0 > planet.velocity.x:
                currentPeriodTime = currentTime - currentPeriodStartTime
                singlePeriodTimeList.append(currentPeriodTime)
                currentPeriodStartTime = currentTime

            if maxTrailLength != -2:
                planetSphere.trail.append(planetSphere.pos)

        for i in range(len(singlePeriodTimeList)):
            print("period " + str(i) + " was " + str(singlePeriodTimeList[i]) + " Earth years.")
            multiplePeriodTime = multiplePeriodTime + singlePeriodTimeList[i]

        averagePeriodTime = multiplePeriodTime / len(singlePeriodTimeList)
        averagePeriodTimeList.append(averagePeriodTime)
        singlePeriodTimeList.clear()
        print("average period for an orbital radius of " + str(currentRadius) + " Earth orbit radii was: " + str(averagePeriodTime) + " Earth years")
        print("\n")
        currentTime = 0
        multiplePeriodTime = 0

    for i in range(len(averagePeriodTimeList)):
        periodSquaredList.append(averagePeriodTimeList[i] ** 2)
        radiusCubedList.append(planetOrbitRadiiList[i] ** 3)

    plt.plot(planetOrbitRadiiList, averagePeriodTimeList, 'b.')
    plt.suptitle("Period length of a planet with increasing orbital radii")
    plt.xlabel("Orbital radius (Earth orbit radii)")
    plt.ylabel("Period length (Earth years)")
    plt.show()
