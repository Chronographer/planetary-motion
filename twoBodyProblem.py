from vpython import *
import numpy as np
import matplotlib.pyplot as plt

""" This program simulates a simple 2-body system. Note that it assumes the effects of the first planet object ("planet") 
on the second planet object ("sun") are so small as to be negligable, so position, velocity, ect, are only computed for 
the "planet" object. Note however that any planet object may be used in place of "planet". """


def run(planet, sun, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, vPlot, numPlot, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    currentTime = 0.0
    sunSphere = sphere(pos=vector(0, 0, 0), radius=sphereSizeList[1], color=color.yellow)
    planetSphere = sphere(pos=planet.position, radius=sphereSizeList[0], texture=textures.earth, shininess=0,)
    gravitationalConstant = (4 * np.pi ** 2) / sun.mass

    plotAreaSweptInterval = timeStep * 10
    plotAreaSweptIntervalTimer = 0
    currentSectorPoint = planet.position
    lastSectorPoint = planet.position
    lastAreaSwept = 0
    areaSwept = 0
    dontPlotTheFirstPointFlag = False

    if numPlot is True:
        timeList = []
        plotList = []
        plotIndex = 0

    if vPlot is True:
        gd = graph(width=750, height=700, title='Variation in Mars orbit with addition of Jupiter', xtitle='Time (Years)', ytitle="distance between mars and other mars (AU's)", fast=False)
        genericPlot = gcurve(color=color.cyan, fast=False)

    if maxTrailLength != -2:
        planetSphere.trail = curve(pos=[planetSphere.pos], color=color.white, radius=trailRadius, retain=maxTrailLength, interval=30)

    while currentTime < endTime:
        if plotAreaSweptIntervalTimer >= plotAreaSweptInterval:
            lastSectorPoint = currentSectorPoint
            currentSectorPoint = planet.position
            lastAreaSwept = areaSwept
            centralAngle = degrees(diff_angle(lastSectorPoint, currentSectorPoint))
            areaSwept = pi * distancePlanetSun ** 2 * (centralAngle / 360)
            plotAreaSweptIntervalTimer = 0
            areaSweptDifference = areaSwept - lastAreaSwept
            if numPlot is True:
                if dontPlotTheFirstPointFlag is False:
                    dontPlotTheFirstPointFlag = True
                else:
                    plotList.append(areaSwept)  # to plot the difference each interval in the area swept in the last 2 intervals, add "areaSweptDifference" to this list instead of "areaSwept"
                    timeList.append(plotIndex)
                    plotIndex = plotIndex + plotAreaSweptInterval

        distancePlanetSun = np.sqrt((planet.position.x ** 2 + planet.position.y ** 2 + planet.position.z ** 2))
        forcePlanetSun = (gravitationalConstant * planet.mass * sun.mass) / (distancePlanetSun ** 2)
        accelerationPlanetSun = forcePlanetSun / planet.mass
        unitPositionVectorPlanetSun = norm(sun.position - planet.position)
        accelerationVectorPlanetSun = accelerationPlanetSun * unitPositionVectorPlanetSun
        accelerationVectorPlanet = accelerationVectorPlanetSun
        planet.velocity = planet.velocity + (accelerationVectorPlanet * timeStep)
        planet.position = planet.position + (planet.velocity * timeStep)
        planetSphere.pos = planet.position
        currentTime = currentTime + timeStep
        plotAreaSweptIntervalTimer = plotAreaSweptIntervalTimer + timeStep
        rate(targetFrameRate)

        if maxTrailLength != -2:
            planetSphere.trail.append(planetSphere.pos)

        if vPlot is True:
           genericPlot.plot(currentTime, distancePlanetSun)

    if numPlot is True:
        plt.plot(timeList, plotList, 'b.')
        plt.suptitle("Difference in area swept by path of planet per unit time")
        plt.xlabel("Time (Earth years)")
        plt.ylabel("Area ((circumferences of Earths orbit)^2)")
        plt.show()
