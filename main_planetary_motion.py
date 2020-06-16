import planetaryData
import planetObjectGenerator
import threeBodyProblem
import twoAndThreeBodyComparison
import twoBodyProblemKeplersSecondLaw
import twoBodyProblemKeplersThirdLaw
import twoBodyProblem
from vpython import *


title = ""  # Put a title here if you want it, or leave it as an empty string to free up ~25 extra pixels vertically to display the animation with.
scene = canvas(title=title, width=1200, height=735, forward=vector(-0, -0, -1))
axisLength = 1
maxTrailLength = -2  # To remove the limit set this to -1, to remove the trail entirely, set this to -2. Otherwise set to a positive integer to taste. Can also be set individually for each planet object, if desired.

timeStep = 0.001 * planetaryData.earthPeriod
targetFrameRate = 2000000
endTime = 5

vPlot = False
numPlot = True

sunObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData("sun"), maxTrailLength)
earthObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData('earth'), maxTrailLength)

twoBodyProblemKeplersThirdLaw.run(earthObject, sunObject, axisLength, targetFrameRate, timeStep, endTime)
#twoBodyProblemAreaSwept.run(earthObject, sunObject, axisLength, targetFrameRate, timeStep, vPlot, numPlot, endTime)
