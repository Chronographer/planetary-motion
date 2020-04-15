import twoBodyProblem                   # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep, <integer> targetFrameRate)
import twoBodyVelocityBasedReference    # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep)
import twoBodyEccentricity              # takes arguments (<float> orbitRadius, <float> orbitPeriod, <float> eccentricity, <integer> maxTrailLength, <integer> timeStep)
import twoBodyVelocityAndPositionBased  # takes arguments (<vector(x,y,z)> initialPosition, <vector(x,y,z)> initialVelocity, <integer> maxTrailLength, <integer> timeStep)
import planetaryData                    # takes argument  (<string> planetName) :: returns <list[<float> orbitRadius, <float> orbitPeriod, <float> eccentricity]>
import threeBodyProblem                 # takes arguments (<object> planetObject1, <object> planetObject2, <object> planetObject3, <float> axisLength, <list[<float> sphere1Size, <float> sphere2Size, <float> sphere3Size>], <integer> maxTrailLength, <float> trailRadius, <float> timeStep, <boolean> makeVpythonPlot, <boolean> makePyPlot)
import planetObjectGenerator            # add in arguments later
import numpy as np
import matplotlib.pyplot as plt
from vpython import *

title = "test scene"
scene = canvas(title=title, width=900, height=650, forward=vector(-0, -0, -1))
timeStep = 0.00001 * planetaryData.earthPeriod
targetFrameRate = 900000000
maxTrailLength = -2  # To remove the limit set this to -1, to remove the trail entirely, set this to -2
planet = "mars"
planetDataList = planetaryData.getPlanetData(planet)
trailRadius = 0.01
axisLength = 4
makeVpythonPlot = False
makeNumPyPlot = True
endTime = 50

sphereSizeList = [0.7, 0.2, 0.4]

earthObject = planetObjectGenerator.planet(planetaryData.getPlanetData("mars"))
jupiterObject = planetObjectGenerator.planet(planetaryData.getPlanetData("jupiter"))
sunObject = planetObjectGenerator.planet(planetaryData.getPlanetData("sun"))

threeBodyData = threeBodyProblem.run(earthObject, jupiterObject, sunObject, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, makeVpythonPlot, makeNumPyPlot, endTime)
twoBodyData = twoBodyProblem.run(planetDataList[0], planetDataList[1], maxTrailLength, timeStep, targetFrameRate, endTime)

differenceList = []
threeBodyCleanList = threeBodyData[1]
twoBodyCleanList = twoBodyData[1]
timeList = threeBodyData[0]
for i in range(len(threeBodyCleanList)):
    difference = threeBodyCleanList[i] - twoBodyCleanList[i]
    differenceList.append(difference)

print(len(differenceList))
print(len(timeList))

plt.plot(timeList, differenceList)
plt.show()





