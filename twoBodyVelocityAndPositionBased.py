from vpython import *
import numpy as np

'''
UNITS
    1 AU = 1.5 x 10^11  meters
    1 year = 3.2 x 10^7 seconds
'''


# def run(orbitRadius, orbitPeriod, maxTrailLength, timeStep):
def run(initialPosition, initialVelocity, maxTrailLength, timeStep):
    axisLength = 5
    earthSize = 0.2
    sunSize = 0.5
    trailRadius = 0

    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)

    sun = sphere(pos=vector(0, 0, 0), radius=sunSize, color=color.yellow)
    earth = sphere(pos=vector(planetPosition.x, planetPosition.y, planetPosition.z), radius=earthSize, color=color.cyan)
    if maxTrailLength != -2:
        earth.trail = curve(pos=[earth.pos], color=color.cyan, radius=trailRadius, retain=maxTrailLength, interval=30)

    planetPosition = initialPosition
    planetVelocity = initialVelocity

    while 1:
        distanceEarthSun = np.sqrt((planetPosition.x ** 2 + planetPosition.y ** 2))
        planetVelocity.x = planetVelocity.x - ((4 * np.pi ** 2 * planetPosition.x) / distanceEarthSun ** 3) * timeStep
        planetVelocity.y = planetVelocity.y - ((4 * np.pi ** 2 * planetPosition.y) / distanceEarthSun ** 3) * timeStep
        planetPosition.x = planetPosition.x + (planetVelocity.x * timeStep)
        planetPosition.y = planetPosition.y + (planetVelocity.y * timeStep)
        rate(60)
        earth.pos = planetPosition
        if maxTrailLength != -2:
            earth.trail.append(earth.pos)
