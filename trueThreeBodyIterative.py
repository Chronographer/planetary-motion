import planetaryData
import planetaryBodyGenerator
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


def run(planetNameList, targetFrameRate, timeStep, endTime, massList, maxTrailLength):
    scene.width = 1200
    scene.height = 800

    for iteration in range(len(massList)):
        planetaryData.setPretendStartParameters(planetaryData.jupiterOrbitRadius, planetaryData.jupiterPeriod, planetaryData.jupiterEccentricity, (planetaryData.jupiterMass * massList[iteration]), planetaryData.jupiterSphereRadius)

        localPlanetObjectList = planetaryBodyGenerator.generatePlanetList(planetNameList, maxTrailLength)
        earth = localPlanetObjectList[0]
        jupiter = localPlanetObjectList[1]
        sun = localPlanetObjectList[2]

        gravitationalConstant = (4 * pi ** 2) / sun.mass
        currentTime = 0.0

        print("starting iteration " + str(iteration))
        print("Jupiter mass is " + str(jupiter.mass))
        print("sun position is " + str(sun.position))
        print("sun velocity is " + str(sun.velocity))
        while currentTime < endTime:
            earth.recordTelemetry(currentTime)
            earth.handlePeriodCounting(currentTime)

            displacementVectorEarthSun = sun.position - earth.position
            displacementVectorJupiterSun = sun.position - jupiter.position
            displacementVectorJupiterEarth = earth.position - jupiter.position

            distanceEarthSun = mag(displacementVectorEarthSun)
            distanceJupiterSun = mag(displacementVectorJupiterSun)
            distanceJupiterEarth = mag(displacementVectorJupiterEarth)

            forceEarthSun = (gravitationalConstant * earth.mass * sun.mass) / (distanceEarthSun ** 2)
            forceJupiterSun = (gravitationalConstant * jupiter.mass * sun.mass) / (distanceJupiterSun ** 2)
            forceJupiterEarth = (gravitationalConstant * jupiter.mass * earth.mass) / (distanceJupiterEarth ** 2)

            accelerationEarthSun = forceEarthSun / earth.mass
            accelerationEarthJupiter = forceJupiterEarth / earth.mass
            accelerationJupiterSun = forceJupiterSun / jupiter.mass
            accelerationJupiterEarth = forceJupiterEarth / jupiter.mass
            accelerationSunEarth = forceEarthSun / sun.mass
            accelerationSunJupiter = forceJupiterSun / sun.mass

            unitPositionVectorEarthSun = norm(displacementVectorEarthSun)
            unitPositionVectorJupiterSun = norm(displacementVectorJupiterSun)
            unitPositionVectorJupiterEarth = norm(displacementVectorJupiterEarth)

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

            rate(targetFrameRate)
        print("Iteration " + str(iteration) + " complete.")
        print("\n")
    print("All iterations complete.")
