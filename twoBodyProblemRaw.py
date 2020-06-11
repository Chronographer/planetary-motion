from vpython import *
import numpy as np
import matplotlib.pyplot as plt

""" This program simulates a simple 2-body system. Note that it assumes the effects of the first planet object ("planet") 
on the second planet object ("sun") are so small as to be negligible, so position, velocity, ect, are only computed for 
the "planet" object. Note however that any planet object may be used in place of "planet" or "sun". """


def run(planet, sun, axisLength, targetFrameRate, timeStep, vPlot, numPlot, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)

    gravitationalConstant = (4 * np.pi ** 2) / sun.mass
    currentTime = 0.0

    if numPlot is True:
        timeList = []
        plotList = []

    if vPlot is True:
        gd = graph(width=750, height=700, title='Insert title here', xtitle='insert x axis label here', ytitle="insert y axis label here", fast=False)
        genericPlot = gcurve(color=color.cyan, fast=False)

    while currentTime < endTime:
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

        if vPlot is True:
            genericPlot.plot(currentTime, distancePlanetSun)

    if numPlot is True:
        plt.plot(timeList, plotList, 'b.')
        plt.suptitle("null")
        plt.xlabel("null")
        plt.ylabel("null")
        plt.show()
