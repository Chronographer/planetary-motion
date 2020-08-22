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
    scene.height = 730

    currentTime = 0.0
    gravitationalConstant = (4 * pi ** 2) / dynamicSun.mass
    """
    Note: 'static' and 'dynamic' refer to the two different versions of the model which are run in this script side by side.
        The terms refer to the sun, which is either A) simulated as a 'static' body which is assumed to be affected by other 
        objects to such a negligible degree that their effects can be ignored (as was the case in Lab 7), or B) simulated
        as a 'dynamic' body, where the effects of the other objects on it are calculated and applied.  
    """
    while currentTime < endTime:
        # *** Dynamic Sun model calculations *** #
        # dynamicEarth.recordTelemetry(currentTime)
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

        # *** Static Sun model calculations *** #
        # staticEarth.recordTelemetry(currentTime)
        staticEarth.handlePeriodCounting(currentTime)

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

    xAxisList = []
    periodDifferenceList = []
    staticEarth.periodLengthList.pop(0)   # For reasons I have not yet discovered, the first recorded period seems to be ~ 1/4 what it should be. As...
    dynamicEarth.periodLengthList.pop(0)  # ... a temporary work around, I just remove the first element so it doesn't throw off anything.
    if len(staticEarth.periodLengthList) > len(dynamicEarth.periodLengthList):  # if the number of elements in these two lists are different, only plot as many points as are in the shorter of the two.
        for i in range(len(dynamicEarth.periodLengthList)):
            xAxisList.append(i)
            periodDifferenceList.append(dynamicEarth.periodLengthList[i] - staticEarth.periodLengthList[i])
    else:
        for i in range(len(staticEarth.periodLengthList)):
            xAxisList.append(i)
            periodDifferenceList.append(dynamicEarth.periodLengthList[i] - staticEarth.periodLengthList[i])

    plt.plot(xAxisList, periodDifferenceList, label="Run time: " + str(endTime) + " Earth years\nJupiter mass: " + str(staticJupiter.mass/trueJupiterMass) + "x real Jupiter mass")
    plt.suptitle("Difference between static and dynamic model\nof sequentially measured orbital orbital period of " + staticEarth.name)
    plt.xlabel("Period number")
    plt.ylabel("Difference in period length (Earth years)")
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

    """
    # *** Uncomment this to plot difference between the static and dynamic Earths position and velocity *** #
    
    dynamicVelocityComponents = extractVectorComponents(dynamicEarth.velocityList)
    dynamicPositionComponents = extractVectorComponents(dynamicEarth.positionList)

    staticVelocityComponents = extractVectorComponents(staticEarth.velocityList)
    staticPositionComponents = extractVectorComponents(staticEarth.positionList)

    dynamicAndStaticEarthPositionDifferenceList = []
    dynamicAndStaticEarthVelocityDifferenceList = []
    for i in range(len(staticEarth.timeList)):
        dynamicAndStaticEarthPositionDifferenceList.append(dynamicPositionComponents[3][i] - staticPositionComponents[3][i])
        dynamicAndStaticEarthVelocityDifferenceList.append(dynamicVelocityComponents[3][i] - staticVelocityComponents[3][i])

    plt.plot(staticEarth.timeList, dynamicAndStaticEarthPositionDifferenceList)
    plt.suptitle("Straight line displacement between static and dynamic Earth")
    plt.xlabel("Time (years)")
    plt.ylabel("Distance between static and dynamic Earth (AU's)")
    # plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    plt.plot(staticEarth.timeList, dynamicAndStaticEarthVelocityDifferenceList, 'r')
    plt.suptitle("Velocity difference between static and dynamic Earth")
    plt.xlabel("Time (years)")
    plt.ylabel("Velocity difference between static and dynamic Earth (AU's/year)")
    # plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    plt.plot(staticEarth.timeList, dynamicAndStaticEarthPositionDifferenceList, label='position')
    plt.plot(staticEarth.timeList, dynamicAndStaticEarthVelocityDifferenceList, 'r', label='velocity')
    plt.suptitle("Velocity and position differences between static and dynamic Earth")
    plt.xlabel("Time (years)")
    plt.ylabel("Difference in position | velocity between static and dynamic Earth (AU's | AU's/year)")
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
    """
