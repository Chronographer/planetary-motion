from planetaryData import jupiterMass as trueJupiterMass
from vpython import *
import matplotlib.pyplot as plt


def extractVectorComponents(vectorList):
    componentList = [[], [], []]
    for i in range(len(vectorList)):
        componentList[0].append(vectorList[i].x)
        componentList[1].append(vectorList[i].y)
        componentList[2].append(vectorList[i].z)
    return componentList


def run(planetObjectList, targetFrameRate, timeStep, endTime):
    earth = planetObjectList[0]
    jupiter = planetObjectList[1]
    sun = planetObjectList[2]

    currentTime = 0.0
    gravitationalConstant = (4 * pi ** 2) / sun.mass

    while currentTime < endTime:
        earth.recordTelemetry(currentTime)
        earth.handlePeriodCounting(currentTime)

        distanceEarthSun = sqrt((earth.position.x ** 2 + earth.position.y ** 2 + earth.position.z ** 2))
        distanceJupiterSun = sqrt((jupiter.position.x ** 2 + jupiter.position.y ** 2 + jupiter.position.z ** 2))
        distanceJupiterEarth = sqrt((earth.position.x - jupiter.position.x) ** 2 + (earth.position.y - jupiter.position.y) ** 2 + (earth.position.z - jupiter.position.z) ** 2)

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

        rate(targetFrameRate)

    velocityComponents = extractVectorComponents(earth.velocityList)
    positionComponents = extractVectorComponents(earth.positionList)
    plt.plot(earth.timeList, velocityComponents[0], label="Jupiter mass: " + str(jupiter.mass/trueJupiterMass) + "x 'real' Jupiter mass")
    plt.xlabel("Time (years)")
    plt.ylabel("Velocity (x component) (AU's per year)")
    plt.suptitle("Earth velocity in the X direction over time")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
