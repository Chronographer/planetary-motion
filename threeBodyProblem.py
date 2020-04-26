from vpython import *
import numpy as np
import matplotlib.pyplot as plt
import positionVectorGenerator
import time


def run(earth, jupiter, sun, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, vPlot, numPlot, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    currentTime = 0.0
    if numPlot == True:
        threeBodyEarthPositionList = []
        timeList = []
    sunSphere = sphere(pos=vector(0, 0, 0), radius=sphereSizeList[2], color=color.yellow)
    earthSphere = sphere(pos=earth.position, radius=sphereSizeList[0], color=color.blue)
    jupiterSphere = sphere(pos=jupiter.position, radius=sphereSizeList[1], color=color.orange)
    if maxTrailLength != -2:
        earthSphere.trail = curve(pos=[earthSphere.pos], color=color.cyan, radius=trailRadius, retain=maxTrailLength, interval=30)
        jupiterSphere.trail = curve(pos=[jupiterSphere.pos], color=color.red, radius=trailRadius, retain=maxTrailLength, interval=30)
    gravitationalConstant = (4 * np.pi ** 2) / sun.mass

    earthPlot = gcurve(color=color.cyan, fast=False)
    jupiterPlot = gcurve(color=color.red, fast=False)

    performanceList = []
    counter = 0
    while currentTime < endTime:
        beginTime = time.perf_counter_ns()
        distanceEarthSun = np.sqrt((earth.position.x ** 2 + earth.position.y ** 2 + earth.position.z ** 2))
        distanceJupiterSun = np.sqrt((jupiter.position.x ** 2 + jupiter.position.y ** 2 + jupiter.position.z ** 2))
        distanceJupiterEarth = np.sqrt((earth.position.x - jupiter.position.x) ** 2 + (earth.position.y - jupiter.position.y) ** 2 + (earth.position.z - jupiter.position.z) ** 2)

        forceEarthSun = (gravitationalConstant * earth.mass * sun.mass) / (distanceEarthSun ** 2)
        forceJupiterSun = (gravitationalConstant * jupiter.mass * sun.mass) / (distanceJupiterSun ** 2)
        forceJupiterEarth = (gravitationalConstant * jupiter.mass * earth.mass) / (distanceJupiterEarth ** 2)

        accelerationEarthSun = forceEarthSun / earth.mass
        accelerationEarthJupiter = forceJupiterEarth / earth.mass
        accelerationJupiterSun = forceJupiterSun / jupiter.mass
        accelerationJupiterEarth = forceJupiterEarth / jupiter.mass

        unitPositionVectorEarthSun = norm(positionVectorGenerator.generatePositionVector(earth, sun))
        unitPositionVectorJupiterSun = norm(positionVectorGenerator.generatePositionVector(jupiter, sun))
        unitPositionVectorJupiterEarth = norm(positionVectorGenerator.generatePositionVector(jupiter, earth))

        accelerationVectorEarthSun = accelerationEarthSun * unitPositionVectorEarthSun
        accelerationVectorEarthJupiter = accelerationEarthJupiter * -unitPositionVectorJupiterEarth
        accelerationVectorJupiterSun = accelerationJupiterSun * unitPositionVectorJupiterSun
        accelerationVectorJupiterEarth = accelerationJupiterEarth * unitPositionVectorJupiterEarth

        accelerationVectorEarth = accelerationVectorEarthJupiter + accelerationVectorEarthSun
        accelerationVectorJupiter = accelerationVectorJupiterEarth + accelerationVectorJupiterSun

        earth.velocity = earth.velocity + (accelerationVectorEarth * timeStep)
        jupiter.velocity = jupiter.velocity + (accelerationVectorJupiter * timeStep)

        earth.position = earth.position + (earth.velocity * timeStep)
        jupiter.position = jupiter.position + (jupiter.velocity * timeStep)

        currentTime = currentTime + timeStep

        finishTime = time.perf_counter_ns()
        #if counter >=1000:
        performanceList.append(finishTime - beginTime)
            #print("iteration " + str(counter - 1000) + " computed in " + str(performanceList[counter - 1000]) + " nanoseconds")
        counter = counter + 1

        earthSphere.pos = earth.position
        jupiterSphere.pos = jupiter.position

        if maxTrailLength != -2:
            earthSphere.trail.append(earthSphere.pos)
            jupiterSphere.trail.append(jupiterSphere.pos)
        if vPlot == True:
            earthPlot.plot(currentTime, earth.velocity.y)
            jupiterPlot.plot(currentTime, jupiter.velocity.x)
        if numPlot == True:
            #timeList.append(currentTime)
            threeBodyEarthPositionList.append(earth.position)
        rate(targetFrameRate)
    returnList = []
    returnList.append(timeList)
    returnList.append(threeBodyEarthPositionList)

    print("average computation time was " + str( (sum(performanceList)) / (len(performanceList)) ) )

    return returnList

