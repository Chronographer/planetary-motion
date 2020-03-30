from vpython import *
import numpy as np
import positionVectorGenerator


def run(earth, jupiter, sun, axisLength, sphereSizeList, maxTrailLength, trailRadius, timeStep):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    sunSphere = sphere(pos=vector(0, 0, 0), radius=sphereSizeList[0], color=color.yellow)
    earthSphere = sphere(pos=earth.position, radius=sphereSizeList[1], color=color.cyan)
    jupiterSphere = sphere(pos=jupiter.position, radius=sphereSizeList[2], color=color.orange)
    if maxTrailLength != -2:
        earthSphere.trail = curve(pos=[earth.pos], color=color.blue, radius=trailRadius, retain=maxTrailLength, interval=30)
        jupiterSphere.trail = curve(pos=[earth.pos], color=color.blue, radius=trailRadius, retain=maxTrailLength, interval=30)

    gravitationalConstant = (4 * np.pi ** 2) / sun.mass
    while 1:
        distanceEarthSun = np.sqrt((earth.position.x ** 2 + earth.position.y ** 2))
        distanceJupiterSun = np.sqrt((jupiter.position.x ** 2 + jupiter.position.y ** 2))
        distanceJupiterEarth = np.sqrt((earth.position.x - jupiter.position.x) ** 2 + (earth.position.y - jupiter.position.y) ** 2)

        forceEarthSun = - (gravitationalConstant * earth.mass * sun.mass) / (distanceEarthSun ** 2)
        forceJupiterSun = - (gravitationalConstant * jupiter.mass * sun.mass) / (distanceJupiterSun ** 2)
        forceJupiterEarth = - (gravitationalConstant * jupiter.mass * earth.mass) / (distanceJupiterEarth ** 2)

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
