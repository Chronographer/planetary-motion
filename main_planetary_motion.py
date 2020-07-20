import planetaryData
import planetObjectGenerator
import threeBodyProblem
import twoAndThreeBodyComparison
import twoBodyProblemKeplersSecondLaw
import twoBodyProblemKeplersThirdLaw
import twoBodyProblem
import trueThreeBodyProblem
from vpython import *


title = ""  # Put a title here if you want it, or leave it as an empty string to free up ~25 extra pixels vertically to display the animation with.
scene = canvas(title=title, width=1200, height=735, forward=vector(-0, -0, -1))
axisLength = 1
maxTrailLength = -1  # To remove the limit set this to -1, to remove the trail entirely, set this to -2. Otherwise set to a positive integer to taste. Can also be set individually for each planet object, if desired.

timeStep = 0.001 * planetaryData.earthPeriod
targetFrameRate = 30
endTime = 5000

vPlot = False
numPlot = False

"""
Note: if any planet objects are not being used for a given simulation, their creation should be commented out below 
because if they are not then they will still be rendered to the display, even though they are not being passed into any
functions, since the planet object actually creates and handles its own vpython sphere object inside of itself. 
"""

sunObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData('sun'), maxTrailLength)
earthObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData('earth'), maxTrailLength)
#marsObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData('mars'), maxTrailLength)
#twoBodyMarsObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData('mars'), maxTrailLength)
jupiterObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData('jupiter'), maxTrailLength)
trueThreeBodyProblem.run(earthObject, jupiterObject, sunObject, axisLength, targetFrameRate, timeStep, vPlot, endTime)


#twoAndThreeBodyComparison.run(marsObject, twoBodyMarsObject, jupiterObject, sunObject, axisLength, targetFrameRate, timeStep, endTime)
#twoBodyProblemKeplersThirdLaw.run(earthObject, sunObject, axisLength, targetFrameRate, timeStep, endTime)
#twoBodyProblemAreaSwept.run(earthObject, sunObject, axisLength, targetFrameRate, timeStep, vPlot, numPlot, endTime)
#twoBodyProblem.run(earthObject, sunObject, axisLength, targetFrameRate, timeStep, vPlot, numPlot, endTime)
