from vpython import *
import numpy as np
import matplotlib.pyplot as plt
import positionVectorGenerator


def run(earth, sun, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, vPlot, numPlot, endTime):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    currentTime = 0.0
    sunSphere = sphere(pos=vector(0, 0, 0), radius=sphereSizeList[0], color=color.yellow)
    earthSphere = sphere(pos=earth.position, radius=sphereSizeList[1], color=color.green)
    gravitationalConstant = (4 * np.pi ** 2) / sun.mass
    gd = graph(width=1500, height=700, title='Variation in Mars orbit with addition of Jupiter', xtitle='Time (Years)', ytitle="distance between mars and other mars (AU's)", fast=False)

    if numPlot is True:
        timeList = []
    if maxTrailLength != -2:
        earthSphere.trail = curve(pos=[earthSphere.pos], color=color.white, radius=trailRadius, retain=50, interval=30)

    while currentTime < endTime:
        distanceEarthSun = np.sqrt((earth.position.x ** 2 + earth.position.y ** 2 + earth.position.z ** 2))
        forceEarthSun = (gravitationalConstant * earth.mass * sun.mass) / (distanceEarthSun ** 2)
        accelerationEarthSun = forceEarthSun / earth.mass
        unitPositionVectorEarthSun = norm(positionVectorGenerator.generatePositionVector(earth, sun))
        accelerationVectorEarthSun = accelerationEarthSun * unitPositionVectorEarthSun
        accelerationVectorEarth = accelerationVectorEarthSun
        earth.velocity = earth.velocity + (accelerationVectorEarth * timeStep)
        earth.position = earth.position + (earth.velocity * timeStep)
        earthSphere.pos = earth.position
        currentTime = currentTime + timeStep
        rate(targetFrameRate)

        if maxTrailLength != -2:
            earthSphere.trail.append(earthSphere.pos)
