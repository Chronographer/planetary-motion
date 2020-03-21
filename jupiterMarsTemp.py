"""Simulation of a 3-body system, with Jupiter and other planet orbiting a fixed Sun.

Rigged to do Jupiter-Earth and Sun system.  Change USER INPUTS to simulate
other systems.

Uses Euler-Cromer system, updating momentum not velocity.
Output is a VPython visual demo.  Printout can be added by commenting out
statement in while loop.

Antonio
Physics 685-4w, Summer 2006
"""
from vpython import *
import time

win = 600  # display window size

# Astronomical units:
#    distance from earth to sun = 1
#    period of one earth orbit (1 year) = 1
#    Makes
#       v of earth =  2 pi AU/yr
#       GMsun = 4\pi^2
year = 3.2e7         # convert time to years if necessary
AU = 1.5e11          # convert  meters to Astronomical Units if necessary
GMsun = 4*pi**2

# table of masses in units of solar mass
SolarMass = 2e30
massSun = 2.0e30 / SolarMass
massMercury = 2.4e23 / SolarMass
massVenus = 4.9e24 / SolarMass
massEarth = 6.0e24 / SolarMass
massMars = 6.6e23 / SolarMass
massJupiter = 1.9e27 / SolarMass
massSaturn = 5.7e26 / SolarMass
massUranus = 8.8e25 / SolarMass
massNeptune = 1.03e26 / SolarMass
massPluto = 6.0e24 / SolarMass

# table of orbital radii in AU
orbital_radius_mercury = 0.39
orbital_radius_venus = 0.72
orbital_radius_earth = 1.001
orbital_radius_mars = 1.52
orbital_radius_jupiter = 5.20
orbital_radius_saturn = 9.54
orbital_radius_uranus = 19.19
orbital_radius_neptune = 30.06
orbital_radius_pluto = 39.53

# table of planetary radii (ADD MORE HERE)
radius_sun = 2e9/AU
radius_earth = 6.4e6/AU
radius_jupiter = 11.2*6.4e6/AU

# USER INPUTS
# pick correct orbital radius of your planet:
# orbital_radius_planet = orbital_radius_mars
orbital_radius_planet = 3.29  # 2:1 Kirkwood gap
# pick correct mass
massPlanet = massMars
# pick a good title
plot_title = "Jupiter + Mars"
# pick planet size for graphics: adjust scale and 2 numbers as desired
scale = 50.0
size_sun = scale*radius_sun
size_planet = scale*40*radius_earth
size_jupiter = scale*20.0*radius_jupiter
# end USER INPUTS

# initial speeds
velocityPlanet = 2 * pi / sqrt(orbital_radius_planet)
velocityJupiter = 2 * pi / sqrt(orbital_radius_jupiter)

# set trail radius
radiusTrail = size_jupiter / 10.0
L = 1.5*orbital_radius_jupiter

# dimensions of scene
scene = canvas(title=plot_title, width=win, height=win, range=2*L, forward=vector(-1,-1,-1))

# axes for plot. pos=[] is a list of points which define the curve.
xaxis = curve(pos=[vector(0,0,0), vector(L,0,0)], color=vector(0.5,0.5,0.5))
yaxis = curve(pos=[vector(0,0,0), vector(0,L,0)], color=vector(0.5,0.5,0.5))
zaxis = curve(pos=[vector(0,0,0), vector(0,0,L)], color=vector(0.5,0.5,0.5))

# initial conditions of planet
earthXPosition, earthYPosition, earthZPosition = orbital_radius_planet, 0., 0.
earthXMomentum, earthYMomentum, earthZMomentum = 0.0, massPlanet * velocityPlanet, 0.0
earthPosition = vector(earthXPosition, earthYPosition, earthZPosition)
earthMomentum = vector(earthXMomentum, earthYMomentum, earthZMomentum)

# initial conditions of jupiter
jupiterXPosition, jupiterYPosition, jupiterZPosition = orbital_radius_jupiter, 0., 0.
jupiterXMomentum, jupiterYMomentum, jupiterZMomentum = 0.0, massJupiter * velocityJupiter, 0.0
jupiterPosition = vector(jupiterXPosition, jupiterYPosition, jupiterZPosition)
jupiterMomentum = vector(jupiterXMomentum, jupiterYMomentum, jupiterZMomentum)

# Graphics
sun = sphere(pos=vector(0, 0, 0), radius=size_sun, color=color.yellow)
planet = sphere(pos=vector(earthXPosition, earthYPosition, earthZPosition), radius=size_planet, color=color.cyan)
planet.trail = curve(pos=[planet.pos], color=color.cyan, radius=radiusTrail)
jupiter = sphere(pos=vector(jupiterXPosition, jupiterYPosition, jupiterZPosition), radius=size_jupiter, color=color.red)
jupiter.trail = curve(pos=[jupiter.pos], color=color.red, radius=radiusTrail)

# prepare Euler-Cromer loop
currentTime = 0.0
timeStep = 5.0e-3
numberOfTimeSteps = 0
startTime = clock()

# Euler loop
print("#Time, planet radius, planet speed")
while 1:
    # Compute all (inter)planetary displacements and distances
    eradius = mag(earthPosition)
    jradius = mag(jupiterPosition)
    ejposition = earthPosition - jupiterPosition
    ejradius = mag(ejposition)

    # Compute all forces on all planets
    forceEarthBySun = -GMsun * massPlanet * earthPosition / eradius ** 3    # force on planet by sun
    forceJupiterBySun = -GMsun * massJupiter * jupiterPosition / jradius ** 3  # force on jupiter by sun
    forceEarthByJupiter = -(GMsun * massJupiter) * massPlanet * ejposition / ejradius ** 3
    # force on planet by jupiter
    # update momenta, then positions
    earthMomentum = earthMomentum + (forceEarthBySun + forceEarthByJupiter) * timeStep
    jupiterMomentum = jupiterMomentum + (forceJupiterBySun - forceEarthByJupiter) * timeStep

    # Having updated all momenta, now update all positions
    earthPosition = earthPosition + (earthMomentum / massPlanet) * timeStep
    jupiterPosition = jupiterPosition + (jupiterMomentum / massJupiter) * timeStep

    currentTime = currentTime + timeStep

    # PRINT out information if desired:
    # print (t, planet.pos.x, planet.pos.y, jupiter.pos.x, jupiter.pos.y)
    # print (t, mag(earthPosition), mag(earthMomentum))

    # Update positions of display objects; add trail
    planet.pos = earthPosition
    jupiter.pos = jupiterPosition
    if numberOfTimeSteps % 10 == 0:
        planet.trail.append(pos=earthPosition)
        jupiter.trail.append(pos=jupiterPosition)

    # timing information
    if numberOfTimeSteps == 1000:
        print('# %5.3f seconds for %d steps, 3 body system' % (clock() - startTime, numberOfTimeSteps))

    numberOfTimeSteps = numberOfTimeSteps + 1
    rate(60)

