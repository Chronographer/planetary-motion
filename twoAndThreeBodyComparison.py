from vpython import *
import numpy as np


"""
This script simultaneously runs a two body and three body simulation and tracks the variance in position between the 
non-jupiter body (usually earth or mars).
"""


def run(earthThreeBody, earthTwoBody, jupiter, sun, axisLength, targetFrameRate, timeStep, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    currentTime = 0.0

    gravitationalConstant = (4 * np.pi ** 2) / sun.mass
    gd = graph(width=1500, height=700, title='Variation in Mars orbit with addition of Jupiter', xtitle='Time (Earth years)', ytitle="distance between mars and other mars (AU's)", fast=False)
    differencePlot = gcurve(color=color.purple, fast=False)
    differenceList = []
    vpythonTimeList = []

    earthTwoBody.sphere.color = color.green  # Make the two body earth a different color for viewing ease.

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

        earthThreeBody.move(earthThreeBody.position + (earthThreeBody.velocity * timeStep))
        earthTwoBody.move(earthTwoBody.position + (earthTwoBody.velocity * timeStep))
        jupiter.move(jupiter.position + (jupiter.velocity * timeStep))

        currentTime = currentTime + timeStep

        distance = np.sqrt((earthThreeBody.position.x - earthTwoBody.position.x) ** 2 + (earthThreeBody.position.y - earthTwoBody.position.y) ** 2 + (earthThreeBody.position.z - earthTwoBody.position.z) ** 2)
        differenceList.append(distance)
        vpythonTimeList.append(currentTime)
        rate(targetFrameRate)

    for index in range(len(differenceList)):
        differencePlot.plot(vpythonTimeList[index], differenceList[index])
