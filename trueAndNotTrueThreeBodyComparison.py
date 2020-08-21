from planetaryData import jupiterMass as trueJupiterMass
import matplotlib.pyplot as plt
from vpython import *


def extractVectorComponents(vectorList):
    componentList = [[], [], [], []]
    for i in range(len(vectorList)):
        componentList[0].append(vectorList[i].x)
        componentList[1].append(vectorList[i].y)
        componentList[2].append(vectorList[i].z)
        componentList[3].append(mag(vectorList[i]))
    return componentList


def run(dynamicPlanetObjectList, staticPlanetObjectList, targetFrameRate, timeStep, endTime):
    dynamicEarth = dynamicPlanetObjectList[0]
    dynamicJupiter = dynamicPlanetObjectList[1]
    dynamicSun = dynamicPlanetObjectList[2]

    staticEarth = staticPlanetObjectList[0]
    staticJupiter = staticPlanetObjectList[1]
    staticSun = staticPlanetObjectList[2]

    staticEarth.sphere.color = color.green
    staticEarth.sphere.trail_color = color.blue
    staticSun.sphere.color = color.orange


    scene.width = 1200  # Sets the window size of the vPython animation. Set to taste.
    scene.height = 800

    currentTime = 0.0
    gravitationalConstant = (4 * pi ** 2) / dynamicSun.mass

    while currentTime < endTime:
        dynamicEarth.recordTelemetry(currentTime)
        dynamicEarth.handlePeriodCounting(currentTime)

        dynamicDisplacementVectorEarthSun = dynamicSun.position - dynamicEarth.position
        dynamicDisplacementVectorJupiterSun = dynamicSun.position - dynamicJupiter.position
        dynamicDisplacementVectorJupiterEarth = dynamicEarth.position - dynamicJupiter.position

        dynamicDistanceEarthSun = mag(dynamicDisplacementVectorEarthSun)
        dynamicDistanceJupiterSun = mag(dynamicDisplacementVectorJupiterSun)
        dynamicDistanceJupiterEarth = mag(dynamicDisplacementVectorJupiterEarth)

        dynamicForceEarthSun = (gravitationalConstant * dynamicEarth.mass * dynamicSun.mass) / (dynamicDistanceEarthSun ** 2)
        dynamicForceJupiterSun = (gravitationalConstant * dynamicJupiter.mass * dynamicSun.mass) / (dynamicDistanceJupiterSun ** 2)
        dynamicForceJupiterEarth = (gravitationalConstant * dynamicJupiter.mass * dynamicEarth.mass) / (dynamicDistanceJupiterEarth ** 2)

        dynamicAccelerationEarthSun = dynamicForceEarthSun / dynamicEarth.mass
        dynamicAccelerationEarthJupiter = dynamicForceJupiterEarth / dynamicEarth.mass
        dynamicAccelerationJupiterSun = dynamicForceJupiterSun / dynamicJupiter.mass
        dynamicAccelerationJupiterEarth = dynamicForceJupiterEarth / dynamicJupiter.mass
        dynamicAccelerationSunEarth = dynamicForceEarthSun / dynamicSun.mass
        dynamicAccelerationSunJupiter = dynamicForceJupiterSun / dynamicSun.mass

        dynamicUnitPositionVectorEarthSun = norm(dynamicDisplacementVectorEarthSun)
        dynamicUnitPositionVectorJupiterSun = norm(dynamicDisplacementVectorJupiterSun)
        dynamicUnitPositionVectorJupiterEarth = norm(dynamicDisplacementVectorJupiterEarth)

        dynamicAccelerationVectorEarthSun = dynamicAccelerationEarthSun * dynamicUnitPositionVectorEarthSun
        dynamicAccelerationVectorEarthJupiter = dynamicAccelerationEarthJupiter * -dynamicUnitPositionVectorJupiterEarth
        dynamicAccelerationVectorJupiterSun = dynamicAccelerationJupiterSun * dynamicUnitPositionVectorJupiterSun
        dynamicAccelerationVectorJupiterEarth = dynamicAccelerationJupiterEarth * dynamicUnitPositionVectorJupiterEarth
        dynamicAccelerationVectorSunJupiter = dynamicAccelerationSunJupiter * -dynamicUnitPositionVectorJupiterSun
        dynamicAccelerationVectorSunEarth = dynamicAccelerationSunEarth * -dynamicUnitPositionVectorEarthSun

        dynamicAccelerationVectorEarth = dynamicAccelerationVectorEarthJupiter + dynamicAccelerationVectorEarthSun
        dynamicAccelerationVectorJupiter = dynamicAccelerationVectorJupiterEarth + dynamicAccelerationVectorJupiterSun
        dynamicAccelerationVectorSun = dynamicAccelerationVectorSunJupiter + dynamicAccelerationVectorSunEarth

        dynamicEarth.velocity = dynamicEarth.velocity + (dynamicAccelerationVectorEarth * timeStep)
        dynamicJupiter.velocity = dynamicJupiter.velocity + (dynamicAccelerationVectorJupiter * timeStep)
        dynamicSun.velocity = dynamicSun.velocity + (dynamicAccelerationVectorSun * timeStep)

        dynamicEarth.move(dynamicEarth.position + (dynamicEarth.velocity * timeStep))
        dynamicJupiter.move(dynamicJupiter.position + (dynamicJupiter.velocity * timeStep))
        dynamicSun.move(dynamicSun.position + (dynamicSun.velocity * timeStep))




        staticDisplacementVectorEarthSun = staticSun.position - staticEarth.position
        staticDisplacementVectorJupiterSun = staticSun.position - staticJupiter.position
        staticDisplacementVectorJupiterEarth = staticJupiter.position - staticEarth.position

        staticDistanceEarthSun = mag(staticDisplacementVectorEarthSun)
        staticDistanceJupiterSun = mag(staticDisplacementVectorJupiterSun)
        staticDistanceJupiterEarth = mag(staticDisplacementVectorJupiterEarth)

        staticForceEarthSun = (gravitationalConstant * staticEarth.mass * staticSun.mass) / (staticDistanceEarthSun ** 2)
        staticForceJupiterSun = (gravitationalConstant * staticJupiter.mass * staticSun.mass) / (staticDistanceJupiterSun ** 2)
        staticForceJupiterEarth = (gravitationalConstant * staticJupiter.mass * staticEarth.mass) / (staticDistanceJupiterEarth ** 2)

        staticAccelerationEarthSun = staticForceEarthSun / staticEarth.mass
        staticAccelerationEarthJupiter = staticForceJupiterEarth / staticEarth.mass
        staticAccelerationJupiterSun = staticForceJupiterSun / staticJupiter.mass
        staticAccelerationJupiterEarth = staticForceJupiterEarth / staticJupiter.mass

        staticUnitPositionVectorEarthSun = norm(staticDisplacementVectorEarthSun)
        staticUnitPositionVectorJupiterSun = norm(staticDisplacementVectorJupiterSun)
        staticUnitPositionVectorJupiterEarth = norm(staticDisplacementVectorJupiterEarth)

        staticAccelerationVectorEarthSun = staticAccelerationEarthSun * staticUnitPositionVectorEarthSun
        staticAccelerationVectorEarthJupiter = staticAccelerationEarthJupiter * -staticUnitPositionVectorJupiterEarth
        staticAccelerationVectorJupiterSun = staticAccelerationJupiterSun * staticUnitPositionVectorJupiterSun
        staticAccelerationVectorJupiterEarth = staticAccelerationJupiterEarth * staticUnitPositionVectorJupiterEarth

        staticAccelerationVectorEarth = staticAccelerationVectorEarthJupiter + staticAccelerationVectorEarthSun
        staticAccelerationVectorJupiter = staticAccelerationVectorJupiterEarth + staticAccelerationVectorJupiterSun

        staticEarth.velocity = staticEarth.velocity + (staticAccelerationVectorEarth * timeStep)
        staticJupiter.velocity = staticJupiter.velocity + (staticAccelerationVectorJupiter * timeStep)

        staticEarth.move(staticEarth.position + (staticEarth.velocity * timeStep))
        staticJupiter.move(staticJupiter.position + (staticJupiter.velocity * timeStep))




        currentTime = currentTime + timeStep

        rate(targetFrameRate)
    print("Done.")

    velocityComponents = extractVectorComponents(dynamicEarth.velocityList)
    # positionComponents = extractVectorComponents(dynamicEarth.positionList)
