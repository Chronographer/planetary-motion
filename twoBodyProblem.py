from vpython import *
import numpy as np


def run(orbitRadius, orbitPeriod, planetMass):
    timeStep = orbitPeriod/1000
    solarGravitationConstant = 4 * (np.pi ** 2)
    currentTime = 0.0
    L = 5.2
    counter = 0
    AU = 1.5e11

    planetSize = 0.2
    sunSize = 0.5
    trailRadius = planetSize/2

    circularSpeed = (2 * np.pi * orbitRadius) / orbitPeriod
    planetPosition = vector(orbitRadius, 0, 0)
    planetVelocity = vector(0, circularSpeed, 0)

    xAxis = curve(pos=[vector(0, 0, 0), vector(L, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, L, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, L)], color=color.blue)

    sun = sphere(pos=vector(0, 0, 0), radius=sunSize, color=color.yellow)
    planet = sphere(pos=vector(planetPosition.x, planetPosition.y, planetPosition.z), radius=planetSize, color=color.cyan)
    planet.trail = curve(pos=[planet.pos], color=color.cyan, radius=trailRadius)

    '''
    Remember: 
    Force = mass * acceleration
    Momentum = mass * velocity
    
    Acceleration = 1st derivative of velocity = 2nd derivative of position
    Velocity = 1st derivative of position = integral of acceleration
    Position = integral of velocity
    
    Newtons law of gravitation:
        F = (gravitationalConstant * sunMass * earthMass) / r ** 2
        where F is the magnitude of the force between the sun and the earth, r is the distance between the sun and earth
    
    x component of gravitational force:
        -(gravitationalConstant * sunMass * earthMass * earthPositionX)/r ** 3
        (y is the same but swapped)
    
    
    UNITS
        1 AU = 1.5 x 10^11  meters
        1 year = 3.2 x 10^7 seconds
         
    
    '''

    while 1: # the problem is I am treating the acceleration as a scalar when it is in fact a vector, even if it is only in one or two of the components, treating it as a scalar implies that it is equal in ALL components.
        planetAcceleration = ((solarGravitationConstant * planetMass) / (orbitRadius ** 2) / planetMass)
        planetVelocity.x = planetVelocity.x + (planetAcceleration * timeStep)
        planetVelocity.y = planetVelocity.y + (planetAcceleration * timeStep)
        #planetVelocity.z = planetVelocity.z + (planetAcceleration * timeStep)
        planetPosition = planetPosition + (planetVelocity * timeStep)
        currentTime = currentTime + timeStep
        counter = counter + 1
        planet.pos = planetPosition

        rate(60)  # note to self: what does rate(x) do exactly? does it make the program run at most x frames/iterations/steps per second? does this apply only to the frame rate and not to how many steps are actually being applied? (3-21-2020, remove when question has been answered)
        planet.trail.append(planet.pos)
