import trueThreeBodyProblem
import planetaryBodyGenerator
from vpython import *

title = ""  # Put a title here if you want it, or leave it as an empty string to free up ~25 extra pixels vertically to display the animation with.
scene = canvas(title=title, width=1200, height=735, forward=vector(-0, -0, -1))

maxTrailLength = -1  # To remove the limit set this to -1, to remove the trail entirely, set this to -2. Otherwise set to a positive integer to taste. Can also be set individually for each planet object, if desired.
targetFrameRate = 4000
timeStep = 0.001
endTime = 100

xAxis = curve(pos=[vector(0, 0, 0), vector(1, 0, 0)], color=color.red)
yAxis = curve(pos=[vector(0, 0, 0), vector(0, 1, 0)], color=color.green)
zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, 1)], color=color.blue)

planetList = ['Earth', 'Pretend', 'Sun']  # List of planets to use in the simulation. 'Sun' MUST be the last element of the list or total momentum will not be 0. All planet names MUST be capitalized.
planetObjectList = planetaryBodyGenerator.generatePlanetList(planetList, maxTrailLength)
trueThreeBodyProblem.run(planetObjectList, targetFrameRate, timeStep, endTime)
