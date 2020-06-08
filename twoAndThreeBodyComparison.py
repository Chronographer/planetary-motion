from vpython import *
import numpy as np
import matplotlib.pyplot as plt


def run(earthThreeBody, earthTwoBody, jupiter, sun, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, vPlot, numPlot, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    currentTime = 0.0

    if numPlot is True:
        threeBodyEarthPositionList = []
        timeList = []

    sunSphere = sphere(pos=vector(0, 0, 0), radius=sphereSizeList[0], color=color.yellow)
    earthThreeBodySphere = sphere(pos=earthThreeBody.position, radius=sphereSizeList[2], color=color.blue)
    earthTwoBodySphere = sphere(pos=earthTwoBody.position, radius=sphereSizeList[2], color=color.green)
    jupiterSphere = sphere(pos=jupiter.position, radius=sphereSizeList[1], color=color.orange)

    if maxTrailLength != -2:
        earthThreeBodySphere.trail = curve(pos=[earthThreeBodySphere.pos], color=color.cyan, radius=trailRadius, retain=maxTrailLength, interval=180)
        earthTwoBodySphere.trail = curve(pos=[earthTwoBodySphere.pos], color=color.white, radius=trailRadius, retain=maxTrailLength, interval=30)
        jupiterSphere.trail = curve(pos=[jupiterSphere.pos], color=color.red, radius=trailRadius, retain=maxTrailLength, interval=30)

    gravitationalConstant = (4 * np.pi ** 2) / sun.mass
    gd = graph(width=1500, height=700, title='Variation in Mars orbit with addition of Jupiter', xtitle='Time (Earth years)', ytitle="distance between mars and other mars (AU's)", fast=False)
    differencePlot = gcurve(color=color.purple, fast=False)
    differenceList = []
    vpythonTimeList = []

    while currentTime < endTime:
        distanceEarthThreeBodySun = np.sqrt((earthThreeBody.position.x ** 2 + earthThreeBody.position.y ** 2 + earthThreeBody.position.z ** 2))
        distanceJupiterSun = np.sqrt((jupiter.position.x ** 2 + jupiter.position.y ** 2 + jupiter.position.z ** 2))
        distanceJupiterEarth = np.sqrt((earthThreeBody.position.x - jupiter.position.x) ** 2 + (earthThreeBody.position.y - jupiter.position.y) ** 2 + (earthThreeBody.position.z - jupiter.position.z) ** 2)
        distanceEarthTwoBodySun = np.sqrt((earthTwoBody.position.x ** 2 + earthTwoBody.position.y ** 2 + earthTwoBody.position.z ** 2))

        forceEarthThreeBodySun = (gravitationalConstant * earthThreeBody.mass * sun.mass) / (distanceEarthThreeBodySun ** 2)
        forceJupiterSun = (gravitationalConstant * jupiter.mass * sun.mass) / (distanceJupiterSun ** 2)
        forceJupiterEarthThreeBody = (gravitationalConstant * jupiter.mass * earthThreeBody.mass) / (distanceJupiterEarth ** 2)
        forceEarthTwoBodySun = (gravitationalConstant * earthTwoBody.mass * sun.mass) / (distanceEarthTwoBodySun ** 2)

        accelerationEarthThreeBodySun = forceEarthThreeBodySun / earthThreeBody.mass
        accelerationEarthThreeBodyJupiter = forceJupiterEarthThreeBody / earthThreeBody.mass
        accelerationJupiterSun = forceJupiterSun / jupiter.mass
        accelerationJupiterEarthThreeBody = forceJupiterEarthThreeBody / jupiter.mass
        accelerationEarthTwoBodySun = forceEarthTwoBodySun / earthTwoBody.mass

        unitPositionVectorEarthThreeBodySun = norm(sun.position - earthThreeBody.position)
        unitPositionVectorJupiterSun = norm(sun.position - jupiter.position)
        unitPositionVectorJupiterEarthThreeBody = norm(earthThreeBody.position - jupiter.position)
        unitPositionVectorEarthTwoBodySun = norm(sun.position - earthTwoBody.position)

        accelerationVectorEarthThreeBodySun = accelerationEarthThreeBodySun * unitPositionVectorEarthThreeBodySun
        accelerationVectorEarthThreeBodyJupiter = accelerationEarthThreeBodyJupiter * -unitPositionVectorJupiterEarthThreeBody
        accelerationVectorJupiterSun = accelerationJupiterSun * unitPositionVectorJupiterSun
        accelerationVectorJupiterEarthThreeBody = accelerationJupiterEarthThreeBody * unitPositionVectorJupiterEarthThreeBody
        accelerationVectorEarthTwoBodySun = accelerationEarthTwoBodySun * unitPositionVectorEarthTwoBodySun

        accelerationVectorEarthThreeBody = accelerationVectorEarthThreeBodyJupiter + accelerationVectorEarthThreeBodySun
        accelerationVectorJupiter = accelerationVectorJupiterEarthThreeBody + accelerationVectorJupiterSun
        accelerationVectorEarthTwoBody = accelerationVectorEarthTwoBodySun

        earthThreeBody.velocity = earthThreeBody.velocity + (accelerationVectorEarthThreeBody * timeStep)
        jupiter.velocity = jupiter.velocity + (accelerationVectorJupiter * timeStep)
        earthTwoBody.velocity = earthTwoBody.velocity + (accelerationVectorEarthTwoBody * timeStep)

        earthThreeBody.position = earthThreeBody.position + (earthThreeBody.velocity * timeStep)
        jupiter.position = jupiter.position + (jupiter.velocity * timeStep)
        earthTwoBody.position = earthTwoBody.position + (earthTwoBody.velocity * timeStep)

        earthThreeBodySphere.pos = earthThreeBody.position
        jupiterSphere.pos = jupiter.position
        earthTwoBodySphere.pos = earthTwoBody.position
        currentTime = currentTime + timeStep

        if maxTrailLength != -2:
            earthThreeBodySphere.trail.append(earthThreeBodySphere.pos)
            earthTwoBodySphere.trail.append(earthTwoBodySphere.pos)
            jupiterSphere.trail.append(jupiterSphere.pos)
        if vPlot is True:
            distance = np.sqrt((earthThreeBody.position.x - earthTwoBody.position.x) ** 2 + (earthThreeBody.position.y - earthTwoBody.position.y) ** 2 + (earthThreeBody.position.z - earthTwoBody.position.z) ** 2)
            differenceList.append(distance)
            vpythonTimeList.append(currentTime)
        rate(targetFrameRate)

    for index in range(len(differenceList)):
        differencePlot.plot(vpythonTimeList[index], differenceList[index])
