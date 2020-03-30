import twoBodyProblem                   # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep)
import twoBodyVelocityBasedReference    # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep)
import twoBodyEccentricity              # takes arguments (<float> orbitRadius, <float> orbitPeriod, <float> eccentricity, <integer> maxTrailLength, <integer> timeStep)
import twoBodyVelocityAndPositionBased  # takes arguments (<vector(x,y,z)> initialPosition, <vector(x,y,z)> initialVelocity, <integer> maxTrailLength, <integer> timeStep)
import planetaryData                    # takes argument  (<string> planetName) :: returns <list[<float> orbitRadius, <float> orbitPeriod, <float> eccentricity]>
import threeBodyProblem                 # add in arguments later
import planetObjectGenerator
import numpy as np
from vpython import *

title = "test scene"
scene = canvas(title=title, width=640, height=480, forward=vector(-0, -0, -1))
timeStep = 0.01 * planetaryData.earthPeriod
targetFrameRate = 60
maxTrailLength = -1  # To remove the limit set this to -1, to remove the trail entirely, set this to -2
planet = "earth"
planetDataList = planetaryData.getPlanetData(planet)
timeStep = 0.01 * planetDataList[1]
trailRadius = 0.1
axisLength = 4

sphereSizeList = [0.7, 0.2, 0.4]

earthObject = planetObjectGenerator.planet(planetaryData.getPlanetData("earth"))
jupiterObject = planetObjectGenerator.planet(planetaryData.getPlanetData("jupiter"))
sunObject = planetObjectGenerator.planet(planetaryData.getPlanetData("sun"))

threeBodyProblem.run(earthObject, jupiterObject, sunObject, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep)
