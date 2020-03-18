from vpython import *
import numpy as np


def run(orbitRadius, orbitPeriod, planetMass):
    timeStep = orbitPeriod/100
    solarGravitationConstant = 4 * (np.pi **2)
    currentTime = 0.0
    L = 5.2
    counter = 0
    AU = 1.5e11

    planetSize = 0.2
    sunSize = 0.5
    trailRadius = planetSize/2

    circularSpeed = (2 * np.pi * orbitRadius) / orbitPeriod
    position = vector(orbitRadius, 0, 0)
    velocity = vector(0, circularSpeed, 0)

    xAxis = curve(pos=[vector(0, 0, 0), vector(L, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, L, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, L)], color=color.blue)

    planetPosition = vector(orbitRadius, 0, 0)
    planetVelocity = vector(0, circularSpeed, 0)

    sun = sphere(pos=vector(0, 0, 0), radius=sunSize, color=color.yellow)
    planet = sphere(pos=vector(planetPosition.x, planetPosition.y, planetPosition.z), radius=planetSize, color=color.cyan)
    planet.trail = curve(pos=[planet.pos], color=color.cyan, radius=trailRadius)

    while 1:
        planetForce = (solarGravitationConstant * planetMass) / (orbitRadius ** 2)
        planetAcceleration = planetForce / planetMass
        planetVelocity.x = planetVelocity.x + (planetAcceleration * timeStep)
        planetVelocity.y = planetVelocity.y + (planetAcceleration * timeStep)
        planetVelocity.z = planetVelocity.z + (planetAcceleration * timeStep)
        planetPosition = planetPosition + (planetVelocity * timeStep)
        currentTime = currentTime + timeStep
        counter = counter + 1
        planet.pos = planetPosition

        rate(5)
        planet.trail.append(planet.pos)
