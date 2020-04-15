from vpython import *
import numpy as np
import matplotlib.pyplot as plt

'''
UNITS
    1 AU = 1.5 x 10^11  meters
    1 year = 3.2 x 10^7 seconds
'''


def run(orbitRadius, orbitPeriod, maxTrailLength, timeStep, targetFrameRate, endTime):
    axisLength = 5
    earthSize = 0.2
    sunSize = 0.5
    trailRadius = 0

    earthVelocity = (2 * np.pi * orbitRadius) / orbitPeriod
    planetPosition = vector(orbitRadius, 0, 0)

    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)

    sun = sphere(pos=vector(0, 0, 0), radius=sunSize, color=color.yellow)
    earth = sphere(pos=vector(planetPosition.x, planetPosition.y, planetPosition.z), radius=earthSize, color=color.cyan)
    if maxTrailLength != -2:
        earth.trail = curve(pos=[earth.pos], color=color.cyan, radius=trailRadius, retain=maxTrailLength, interval=30)
    earthPosition = vector(orbitRadius, 0, 0)
    earthVelocity = vector(0, earthVelocity, 0)

    currentTime = 0.0
    twoBodyEarthPositionList = []
    timeList = []

    while currentTime < endTime:
        distanceEarthSun = np.sqrt((earthPosition.x ** 2 + earthPosition.y ** 2))
        earthVelocity.x = earthVelocity.x - ((4 * np.pi ** 2 * earthPosition.x) / distanceEarthSun ** 3) * timeStep
        earthVelocity.y = earthVelocity.y - ((4 * np.pi ** 2 * earthPosition.y) / distanceEarthSun ** 3) * timeStep
        earthPosition.x = earthPosition.x + (earthVelocity.x * timeStep)
        earthPosition.y = earthPosition.y + (earthVelocity.y * timeStep)
        rate(targetFrameRate)
        currentTime = currentTime + timeStep
        earth.pos = earthPosition
        twoBodyEarthPositionList.append(earth.pos.x)
        timeList.append(currentTime)

        if maxTrailLength != -2:
            earth.trail.append(earth.pos)
    returnList = []
    returnList.append(timeList)
    returnList.append(twoBodyEarthPositionList)
    return returnList