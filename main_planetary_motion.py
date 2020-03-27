import twoBodyProblem                   # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep)
import twoBodyVelocityBasedReference    # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep)
import twoBodyEccentricity              # takes arguments (<float> orbitRadius, <float> orbitPeriod, <float> eccentricity, <integer> maxTrailLength, <integer> timeStep)
import twoBodyVelocityAndPositionBased  # takes arguments (<vector(x,y,z)> initialPosition, <vector(x,y,z)> initialVelocity, <integer> maxTrailLength, <integer> timeStep)
import planetaryData                    # takes argument  (<string> planetName) :: returns <list[<float> orbitRadius, <float> orbitPeriod, <float> eccentricity]>
import numpy as np
from vpython import *

title = "test scene"
scene = canvas(title=title, width=640, height=480, forward=vector(-0, -0, -1))
timeStep = 0.01 * planetaryData.earthPeriod
targetFrameRate = 960
maxTrailLength = -1  # To remove the limit set this to -1, to remove the trail entirely, set this to -2
planet = "earth"
planetDataList = planetaryData.getPlanetData(planet)


# twoBodyEccentricity.run(planetDataList[0], planetDataList[1], planetDataList[2], maxTrailLength, timeStep, targetFrameRate)
twoBodyVelocityBasedReference.run(planetDataList[0], planetDataList[1], maxTrailLength, timeStep)
