from vpython import *
import numpy as np


def run(earth, jupiter, sun, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, vPlot, numPlot, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    """
    sunSphere = sphere(pos=vector(0, 0, 0), radius=sphereSizeList[0], color=color.yellow)
    earthSphere = sphere(pos=earth.position, radius=sphereSizeList[1], color=color.blue)
    jupiterSphere = sphere(pos=jupiter.position, radius=sphereSizeList[2], color=color.orange)
    if maxTrailLength != -2:
        earthSphere.trail = curve(pos=[earthSphere.pos], color=color.cyan, radius=trailRadius, retain=maxTrailLength, interval=30)
        jupiterSphere.trail = curve(pos=[jupiterSphere.pos], color=color.red, radius=trailRadius, retain=maxTrailLength, interval=30)
    """
    currentTime = 0.0
    gravitationalConstant = (4 * np.pi ** 2) / sun.mass
    if vPlot is True:
        earthPlot = gcurve(color=color.cyan, fast=False)
        jupiterPlot = gcurve(color=color.red, fast=False)

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

        unitPositionVectorEarthSun = norm(sun.position - earth.position)
        unitPositionVectorJupiterSun = norm(sun.position - jupiter.position)
        unitPositionVectorJupiterEarth = norm(earth.position - jupiter.position)

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

        earth.move()
        jupiter.move()
        """
        earthSphere.pos = earth.position
        jupiterSphere.pos = jupiter.position

        if maxTrailLength != -2:
            earthSphere.trail.append(earthSphere.pos)
            jupiterSphere.trail.append(jupiterSphere.pos)
            """
        if vPlot is True:
            earthPlot.plot(currentTime, earth.velocity.y)
            jupiterPlot.plot(currentTime, jupiter.velocity.x)
        rate(targetFrameRate)
