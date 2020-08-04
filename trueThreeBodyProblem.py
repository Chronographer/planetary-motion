from vpython import *
import matplotlib.pyplot as plt

def run(planetObjectList, targetFrameRate, timeStep, endTime):
    earth = planetObjectList[0]
    jupiter = planetObjectList[1]
    sun = planetObjectList[2]

    currentTime = 0.0
    gravitationalConstant = (4 * pi ** 2) / sun.mass

    while currentTime < endTime:
        earth.recordTelemetry(currentTime)

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
    vectorComponent = earth.extractVectorComponent(earth.velocityList)
    plt.plot(earth.timeList, vectorComponent[1])
    plt.xlabel("Time (years)")
    plt.ylabel("Velocity (AU's per year)")
    plt.grid(True)
    plt.show()
