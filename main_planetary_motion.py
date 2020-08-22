import trueThreeBodyProblem
import trueThreeBodyIterative
import trueAndNotTrueThreeBodyComparison
import planetaryBodyGenerator
import planetObjectGenerator
import planetaryData
from vpython import *

title = ""  # Put a title here if you want it, or leave it as an empty string to free up ~25 extra pixels vertically to display the animation with.
# scene = canvas(title=title, width=1200, height=735, forward=vector(-0, -0, -1))

maxTrailLength = -2  # To remove the limit set this to -1, to remove the trail entirely, set this to -2. Otherwise set to a positive integer to taste. Can also be set individually for each planet object, if desired.
targetFrameRate = 500000
timeStep = 0.001
endTime = 200

xAxis = curve(pos=[vector(0, 0, 0), vector(1, 0, 0)], color=color.red)
yAxis = curve(pos=[vector(0, 0, 0), vector(0, 1, 0)], color=color.green)
zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, 1)], color=color.blue)

localPretendMass = planetaryData.jupiterMass * 1

planetaryData.setPretendStartParameters(planetaryData.pretendOrbitRadius, planetaryData.pretendPeriod, planetaryData.pretendEccentricity, localPretendMass, planetaryData.pretendSphereRadius)

planetList = ['Earth', 'Pretend', 'Sun']  # List of planets to use in the simulation. 'Sun' MUST be the last element of the list or total momentum will not be 0. All planet names MUST be capitalized.
massList = []
for i in range(1, 101):
    massList.append(i)

staticEarthObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData('Earth'), maxTrailLength)
staticJupiterObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData('Jupiter'), maxTrailLength)
staticSunObject = planetObjectGenerator.makePlanet(planetaryData.getPlanetData('Sun'), maxTrailLength)

staticPlanetObjectList = [staticEarthObject, staticJupiterObject, staticSunObject]
dynamicPlanetObjectList = planetaryBodyGenerator.generatePlanetList(planetList, maxTrailLength)

trueAndNotTrueThreeBodyComparison.run(dynamicPlanetObjectList, staticPlanetObjectList, targetFrameRate, timeStep, endTime)

# trueThreeBodyProblem.run(planetObjectList, targetFrameRate, timeStep, endTime)
# trueThreeBodyIterative.run(planetList, targetFrameRate, timeStep, endTime, massList, maxTrailLength)
