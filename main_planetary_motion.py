import planetaryData
import planetObjectGenerator
import threeBodyProblem
import twoAndThreeBodyComparison
import twoBodyProblemAreaSwept
import twoBodyProblemPeriodAndRadiusRelationship
import twoBodyProblem
from vpython import *


title = ""  # Put a title here if you want it, or leave it as an empty string to free up ~25 extra pixels vertically to display the animation with.
scene = canvas(title=title, width=1200, height=735, forward=vector(-0, -0, -1))
axisLength = 1
maxTrailLength = -1  # To remove the limit set this to -1, to remove the trail entirely, set this to -2. Otherwise set to a positive integer to taste. Can also be set individually for each planet object, if desired.

timeStep = 0.015 * planetaryData.earthPeriod
targetFrameRate = 2000
endTime = 5000

makeVpythonPlot = False
makeNumPyPlot = False

sunObject = planetObjectGenerator.planet(planetaryData.getPlanetData("sun"), maxTrailLength)
earthObject = planetObjectGenerator.planet(planetaryData.getPlanetData('earth'), maxTrailLength)

twoBodyProblem.run(earthObject, sunObject, axisLength, targetFrameRate, timeStep, makeVpythonPlot, makeNumPyPlot, endTime)

