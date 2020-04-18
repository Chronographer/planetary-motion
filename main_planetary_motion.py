import twoBodyProblem                   # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep, <integer> targetFrameRate)
import twoBodyVelocityBasedReference    # takes arguments (<float> orbitRadius, <float> orbitPeriod, <integer> maxTrailLength, <integer> timeStep)
import twoBodyEccentricity              # takes arguments (<float> orbitRadius, <float> orbitPeriod, <float> eccentricity, <integer> maxTrailLength, <integer> timeStep)
import twoBodyVelocityAndPositionBased  # takes arguments (<vector(x,y,z)> initialPosition, <vector(x,y,z)> initialVelocity, <integer> maxTrailLength, <integer> timeStep)
import planetaryData                    # takes argument  (<string> planetName) :: returns <list[<float> orbitRadius, <float> orbitPeriod, <float> eccentricity]>
import threeBodyProblem                 # takes arguments (<object> planetObject1, <object> planetObject2, <object> planetObject3, <float> axisLength, <list[<float> sphere1Size, <float> sphere2Size, <float> sphere3Size>], <integer> maxTrailLength, <float> trailRadius, <float> timeStep, <boolean> makeVpythonPlot, <boolean> makePyPlot)
import planetObjectGenerator            # add in arguments later
import twoAndThreeBodyComparison
import twoBodyProblemNew
import numpy as np
import matplotlib.pyplot as plt
from vpython import *

title = "test scene"
scene = canvas(title=title, width=900, height=650, forward=vector(-0, -0, -1))
timeStep = 0.005 * planetaryData.earthPeriod
targetFrameRate = 4000
maxTrailLength = -2  # To remove the limit set this to -1, to remove the trail entirely, set this to -2
planet = "mars"
planetDataList = planetaryData.getPlanetData(planet)
trailRadius = 0.01
axisLength = 4
makeVpythonPlot = True
makeNumPyPlot = False
endTime = 1000
sphereSizeList = [0.7, 0.2, 0.4]

earthObject = planetObjectGenerator.planet(planetaryData.getPlanetData(planet))
twoBodyEarth = planetObjectGenerator.planet(planetaryData.getPlanetData(planet))
jupiterObject = planetObjectGenerator.planet(planetaryData.getPlanetData("jupiter"))
sunObject = planetObjectGenerator.planet(planetaryData.getPlanetData("sun"))

#twoAndThreeBodyComparison.run(earthObject, twoBodyEarth, jupiterObject, sunObject, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, makeVpythonPlot, makeNumPyPlot, endTime)

twoBodyProblemNew.run(earthObject, sunObject, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, makeVpythonPlot, makeNumPyPlot, endTime)


"""threeBodyData = threeBodyProblem.run(earthObject, jupiterObject, sunObject, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, makeVpythonPlot, makeNumPyPlot, endTime)
twoBodyData = twoBodyProblem.run(planetDataList[0], planetDataList[1], maxTrailLength, timeStep, targetFrameRate, endTime)

differenceList = []
threeBodyPositionVectorList = threeBodyData[1]
twoBodyPositionVectorList = twoBodyData[1]
timeList = twoBodyData[0]
for i in range(len(threeBodyPositionVectorList)):
    threeBodyVector = threeBodyPositionVectorList[i]
    twoBodyVector = twoBodyPositionVectorList[i]
    distance = np.sqrt((threeBodyVector.x - twoBodyVector.x) ** 2 + (threeBodyVector.y - twoBodyVector.y) ** 2 + (threeBodyVector.z - twoBodyVector.z) ** 2)
    differenceList.append(distance)

plt.plot(timeList, differenceList)
plt.suptitle("Variation between Mars in two and three body computations")
plt.xlabel("Time (Earth years)")
plt.ylabel("Distance (AU's)")
plt.show()"""





