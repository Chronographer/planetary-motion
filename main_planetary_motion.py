import twoBodyProblemDeprecated         # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep, <integer> targetFrameRate)
import twoBodyVelocityBasedReference    # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep)
import twoBodyEccentricity              # takes arguments (<float> orbitRadius, <float> orbitPeriod, <float> eccentricity, <integer> maxTrailLength, <integer> timeStep)
import twoBodyVelocityAndPositionBased  # takes arguments (<vector(x,y,z)> initialPosition, <vector(x,y,z)> initialVelocity, <integer> maxTrailLength, <integer> timeStep)
import planetaryData                    # takes argument  (<string> planetName) :: returns <list[<float> orbitRadius, <float> orbitPeriod, <float> eccentricity]>
import threeBodyProblem                 # takes arguments (<object> planetObject1, <object> planetObject2, <object> planetObject3, <float> axisLength, <list[<float> sphere1Size, <float> sphere2Size, <float> sphere3Size>], <integer> maxTrailLength, <float> trailRadius, <float> timeStep, <boolean> makeVpythonPlot, <boolean> makePyPlot)
import planetObjectGenerator            # add in arguments later
import nBodyExperimental
import twoAndThreeBodyComparison
import twoBodyProblemNew                # takes arguments (<object> planetObject1, <object> planetObject2, <float> axisLength, <list> sphereSizeList[<float> planet1Radius, <float> planet2Radius], <integer> maxTrailLength, <float> trailRadius, <integer> targetFrameRate, <float> timeStep, <boolean> makeVpythonPlot, <boolean> makeNumPyPlot, <float> endTime)
import twoBodyProblemPeriodAndRadiusRelationship
import numpy as np
import matplotlib.pyplot as plt
from vpython import *


title = ""  # Put a title here if you want it, or leave it as an empty string to free up 25 extra pixels vertically to display the animation with.
scene = canvas(title=title, width=1500, height=735, forward=vector(-0, -0, -1))
axisLength = 1
maxTrailLength = -2  # To remove the limit set this to -1, to remove the trail entirely, set this to -2.
trailRadius = 0
sphereSizeList = [0.1, 0.3]

timeStep = 0.001 * planetaryData.earthPeriod
targetFrameRate = 1000000000000
endTime = 5

makeVpythonPlot = False
makeNumPyPlot = True

sunObject = planetObjectGenerator.planet(planetaryData.getPlanetData("sun"))
earthObject = planetObjectGenerator.planet(planetaryData.getPlanetData("earth"))
marsObject = planetObjectGenerator.planet(planetaryData.getPlanetData("mars"))
jupiterObject = planetObjectGenerator.planet(planetaryData.getPlanetData("jupiter"))


twoBodyProblemPeriodAndRadiusRelationship.run(earthObject, sunObject, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, endTime)





