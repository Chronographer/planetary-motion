import twoBodyProblem
import numpy as np
from vpython import *

title = "test scene"
scene = canvas(title=title, width=640, height=480, forward=vector(-1, -1, -1))

year = 3.2e7         # convert time to years if necessary
AU = 1.5e11          # convert  meters to Astronomical Units if necessary
GMsun = 4*pi**2

timeStep = 0.01

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

twoBodyProblem.run(orbital_radius_earth, 1, timeStep)
