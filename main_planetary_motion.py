import planetaryData                    # takes argument  (<string> planetName) :: returns <list[<float> orbitRadius, <float> orbitPeriod, <float> eccentricity]>
import planetObjectGenerator            # add in arguments later
import threeBodyProblem                 # takes arguments (<object> planetObject1, <object> planetObject2, <object> planetObject3, <float> axisLength, <list[<float> sphere1Size, <float> sphere2Size, <float> sphere3Size>], <integer> maxTrailLength, <float> trailRadius, <float> timeStep, <boolean> makeVpythonPlot, <boolean> makePyPlot)
import twoAndThreeBodyComparison
import twoBodyProblem                   # takes arguments (<object> planetObject1, <object> planetObject2, <float> axisLength, <list> sphereSizeList[<float> planet1Radius, <float> planet2Radius], <integer> maxTrailLength, <float> trailRadius, <integer> targetFrameRate, <float> timeStep, <boolean> makeVpythonPlot, <boolean> makeNumPyPlot, <float> endTime)
import twoBodyProblemPeriodAndRadiusRelationship
from vpython import *


title = ""  # Put a title here if you want it, or leave it as an empty string to free up ~25 extra pixels vertically to display the animation with.
scene = canvas(title=title, width=1200, height=735, forward=vector(-0, -0, -1))
axisLength = 1
maxTrailLength = -2  # To remove the limit set this to -1, to remove the trail entirely, set this to -2. Otherwise set to a positive integer to taste. Can also be set individually for each planet object, if desired.

timeStep = 0.01 * planetaryData.earthPeriod
targetFrameRate = 2500000000000
endTime = 5

makeVpythonPlot = True
makeNumPyPlot = False

sunObject = planetObjectGenerator.planet(planetaryData.getPlanetData("sun"), maxTrailLength)
#marsObject = planetObjectGenerator.planet(planetaryData.getPlanetData("mars"), maxTrailLength)
#jupiterObject = planetObjectGenerator.planet(planetaryData.getPlanetData("jupiter"), maxTrailLength)
earthObject = planetObjectGenerator.planet(planetaryData.getPlanetData('earth'), maxTrailLength)

twoBodyProblemPeriodAndRadiusRelationship.run(earthObject, sunObject, axisLength, targetFrameRate, timeStep, endTime)
#threeBodyProblem.run(marsObject, jupiterObject, sunObject, axisLength, targetFrameRate, timeStep, makeVpythonPlot, endTime)
