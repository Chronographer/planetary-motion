from vpython import *
import numpy as np
import matplotlib.pyplot as plt
""" 
This program verifies Kepler's third Law, that the orbital period squared is linearly proportional to the orbital 
radius cubed.

NOTE: 'endTime' behaves differently in this script than in others. Normally, a simulation is terminated after
currentTime exceeds endTime. However in this script, the simulation is not terminated after a certain period of time 
has passed, but instead terminates after a certain number of periods have been simulated. In other words, if 'endTime' 
is 5, this script will run a simulation of multiple different systems (one for each orbital radius value stored in 
planetOrbitRadiiList[], which is populated at run time). Each of these simulations will not run for 5 years, as 
they would in other scripts, but for 5 periods, regardless of the time required for a planet to complete a single
period of motion. This is to prevent a planet from having an "incomplete" orbit included in the average time for each
period, thus distorting the results.  
"""


def run(planet, sun, axisLength, targetFrameRate, timeStep, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)

    currentTime = 0
    gravitationalConstant = (4 * np.pi ** 2) / sun.mass
    singlePeriodTimeList = []
    averagePeriodTimeList = []
    periodSquaredList = []
    radiusCubedList = []

    multiplePeriodTime = 0

    orbitRadiusListPopulator = 1
    maxOrbitRadius = 30
    orbitRadiusIncrement = 1
    planetOrbitRadiiList = []

    while orbitRadiusListPopulator <= maxOrbitRadius:
        planetOrbitRadiiList.append(orbitRadiusListPopulator)
        orbitRadiusListPopulator = orbitRadiusListPopulator + orbitRadiusIncrement

    for index in range(len(planetOrbitRadiiList)):
        currentRadius = planetOrbitRadiiList[index]
        initialVelocity = np.sqrt((4 * pi ** 2) / currentRadius)
        planet.velocity = vector(vector(0, initialVelocity, 0))
        planet.position = vector(currentRadius, 0, 0)
        currentPeriodStartTime = currentTime

        while len(singlePeriodTimeList) < endTime:
            lastXVelocity = planet.velocity.x
            distancePlanetSun = np.sqrt((planet.position.x ** 2 + planet.position.y ** 2 + planet.position.z ** 2))
            forcePlanetSun = (gravitationalConstant * planet.mass * sun.mass) / (distancePlanetSun ** 2)
            accelerationPlanetSun = forcePlanetSun / planet.mass
            unitPositionVectorPlanetSun = norm(sun.position - planet.position)
            accelerationVectorPlanetSun = accelerationPlanetSun * unitPositionVectorPlanetSun
            accelerationVectorPlanet = accelerationVectorPlanetSun
            planet.velocity = planet.velocity + (accelerationVectorPlanet * timeStep)
            planet.move(planet.position + (planet.velocity * timeStep))
            currentTime = currentTime + timeStep
            rate(targetFrameRate)

            if lastXVelocity > 0 > planet.velocity.x:
                currentPeriodTime = currentTime - currentPeriodStartTime
                singlePeriodTimeList.append(currentPeriodTime)
                currentPeriodStartTime = currentTime

        for i in range(len(singlePeriodTimeList)):
            #print("period " + str(i) + " was " + str(singlePeriodTimeList[i]) + " Earth years.")
            multiplePeriodTime = multiplePeriodTime + singlePeriodTimeList[i]

        averagePeriodTime = multiplePeriodTime / len(singlePeriodTimeList)
        averagePeriodTimeList.append(averagePeriodTime)
        singlePeriodTimeList.clear()
        print("average period for an orbital radius of " + str(currentRadius) + " AU's was: " + str(averagePeriodTime) + " Earth years")
        #print("\n")
        currentTime = 0
        multiplePeriodTime = 0

    for i in range(len(averagePeriodTimeList)):
        periodSquaredList.append(averagePeriodTimeList[i] ** 2)
        radiusCubedList.append(planetOrbitRadiiList[i] ** 3)

    # plt.plot(planetOrbitRadiiList, averagePeriodTimeList, label="time step: " + str(timeStep) + " years")  # use this to plot the period time vs orbit radius
    plt.plot(periodSquaredList, radiusCubedList, label="time step: " + str(timeStep) + " years")  # use this to plot the period squared vs the orbit radius cubed
    plt.suptitle("Period length of a planet with increasing orbital radii")
    plt.xlabel("Orbital radius (AU's)")
    plt.ylabel("Period length (Earth years)")
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
