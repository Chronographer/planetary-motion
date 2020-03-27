import twoBodyProblem
import twoBodyVelocityBasedReference
import twoBodyEccentricity
import planetaryData
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
