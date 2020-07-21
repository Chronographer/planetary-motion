from vpython import *
import numpy as np


def run(planetObjectList, targetFrameRate, timeStep, vPlot, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(1, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, 1, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, 1)], color=color.blue)

    earth = planetObjectList[0]
    jupiter = planetObjectList[1]
    sun = planetObjectList[2]

    if vPlot is True:
        earthPlot = gcurve(color=color.cyan, fast=False)
        jupiterPlot = gcurve(color=color.red, fast=False)

    currentTime = 0.0
    gravitationalConstant = (4 * np.pi ** 2) / sun.mass

    sun.velocity = -((earth.mass * earth.velocity) + (jupiter.mass * jupiter.velocity)) / sun.mass
    print("sun velocity is " + str(sun.velocity))
    sun.position.x = -(((earth.mass * earth.position.x) + (jupiter.mass * jupiter.position.x)) / sun.mass)
    print("sun position is " + str(sun.position))

    while currentTime < endTime:

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
        accelerationSunEarth = forceEarthSun / sun.mass
        accelerationSunJupiter = forceJupiterSun / sun.mass

        unitPositionVectorEarthSun = norm(sun.position - earth.position)
        unitPositionVectorJupiterSun = norm(sun.position - jupiter.position)
        unitPositionVectorJupiterEarth = norm(earth.position - jupiter.position)

        accelerationVectorEarthSun = accelerationEarthSun * unitPositionVectorEarthSun
        accelerationVectorEarthJupiter = accelerationEarthJupiter * -unitPositionVectorJupiterEarth
        accelerationVectorJupiterSun = accelerationJupiterSun * unitPositionVectorJupiterSun
        accelerationVectorJupiterEarth = accelerationJupiterEarth * unitPositionVectorJupiterEarth
        accelerationVectorSunJupiter = accelerationSunJupiter * -unitPositionVectorJupiterSun
        accelerationVectorSunEarth = accelerationSunEarth * -unitPositionVectorEarthSun

        accelerationVectorEarth = accelerationVectorEarthJupiter + accelerationVectorEarthSun
        accelerationVectorJupiter = accelerationVectorJupiterEarth + accelerationVectorJupiterSun
        accelerationVectorSun = accelerationVectorSunJupiter + accelerationVectorSunEarth

        earth.velocity = earth.velocity + (accelerationVectorEarth * timeStep)
        jupiter.velocity = jupiter.velocity + (accelerationVectorJupiter * timeStep)
        sun.velocity = sun.velocity + (accelerationVectorSun * timeStep)

        earth.move(earth.position + (earth.velocity * timeStep))
        jupiter.move(jupiter.position + (jupiter.velocity * timeStep))
        sun.move(sun.position + (sun.velocity * timeStep))

        currentTime = currentTime + timeStep

        if vPlot is True:
            earthPlot.plot(currentTime, earth.velocity.y)
            jupiterPlot.plot(currentTime, jupiter.velocity.x)
        rate(targetFrameRate)
