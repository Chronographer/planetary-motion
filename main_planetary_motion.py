import planetaryData
import trueThreeBodyProblem
import planetaryBodyGenerator
from vpython import *

title = ""  # Put a title here if you want it, or leave it as an empty string to free up ~25 extra pixels vertically to display the animation with.
scene = canvas(title=title, width=1200, height=735, forward=vector(-0, -0, -1))

maxTrailLength = -1  # To remove the limit set this to -1, to remove the trail entirely, set this to -2. Otherwise set to a positive integer to taste. Can also be set individually for each planet object, if desired.
targetFrameRate = 3000
timeStep = 0.001 * planetaryData.earthPeriod
endTime = 5000

xAxis = curve(pos=[vector(0, 0, 0), vector(1, 0, 0)], color=color.red)
yAxis = curve(pos=[vector(0, 0, 0), vector(0, 1, 0)], color=color.green)
zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, 1)], color=color.blue)

planetList = ['earth', 'jupiter', 'sun']
planetObjectList = planetaryBodyGenerator.generatePlanetList(planetList, maxTrailLength)
trueThreeBodyProblem.run(planetObjectList, targetFrameRate, timeStep, endTime)
