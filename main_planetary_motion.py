import twoBodyEccentricity              # takes arguments (<float> orbitRadius, <float> orbitPeriod, <float> eccentricity, <integer> maxTrailLength, <integer> timeStep)
import planetaryData                    # takes argument  (<string> planetName) :: returns <list[<float> orbitRadius, <float> orbitPeriod, <float> eccentricity]>
import threeBodyProblem                 # takes arguments (<object> planetObject1, <object> planetObject2, <object> planetObject3, <float> axisLength, <list[<float> sphere1Size, <float> sphere2Size, <float> sphere3Size>], <integer> maxTrailLength, <float> trailRadius, <float> timeStep, <boolean> makeVpythonPlot, <boolean> makePyPlot)
import planetObjectGenerator            # add in arguments later
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
sphereSizeList = [0.3, 0.2, 0.1]

timeStep = 0.001 * planetaryData.earthPeriod
targetFrameRate = 240
endTime = 300

makeVpythonPlot = True
makeNumPyPlot = False

sunObject = planetObjectGenerator.planet(planetaryData.getPlanetData("sun"))
marsObject = planetObjectGenerator.planet(planetaryData.getPlanetData("mars"))
twoBodyMarsObject = planetObjectGenerator.planet(planetaryData.getPlanetData("mars"))
jupiterObject = planetObjectGenerator.planet(planetaryData.getPlanetData("jupiter"))


twoAndThreeBodyComparison.run(marsObject, twoBodyMarsObject, jupiterObject, sunObject, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, makeVpythonPlot, makeNumPyPlot, endTime)




