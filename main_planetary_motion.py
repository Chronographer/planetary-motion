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
import numpy as np
import matplotlib.pyplot as plt
from vpython import *

# The following variables set basic parameters related to the vpython animation itself.
title = "test scene"
scene = canvas(title=title, width=900, height=650, forward=vector(-0, -0, -1))
axisLength = 4       # Specify how long to make the x-y-z axises.

# The following variables control aesthetic/visual aspects of the planets in the animation.
maxTrailLength = -1  # To remove the limit set this to -1, to remove the trail entirely, set this to -2. (excessively long or unrestricted trail lengths can cause the animation to lag over time)
trailRadius = 0      # Specify the radius of the trail left behind the planets.
sphereSizeList = [0.1, 0.5]  # determines the radius of each of the planets in the various simulations

# These tell a simulation if they should display various plots. Exactly what these are plotting when enabled is controlled within each python file. Not all programs use these.
makeVpythonPlot = True
makeNumPyPlot = False

# These deal with the nuts and bolts of how fast and how long the simulation is run for.
timeStep = 0.005 * planetaryData.earthPeriod
targetFrameRate = 30  # how fast the simulation is run at in time-steps/second. Note that this does not guarantee that it will actually attain this speed, just that it will not exceed it.
endTime = 1000  # How long to run the simulation before stopping it. (numpy plots will not display until the simulation is finished) Not all programs use this.

twoBodyEarth = planetObjectGenerator.planet(planetaryData.getPlanetData("earth"))

sunObject = planetObjectGenerator.planet(planetaryData.getPlanetData("sun"))
mercuryObject = planetObjectGenerator.planet(planetaryData.getPlanetData("mercury"))
venusObject = planetObjectGenerator.planet(planetaryData.getPlanetData("venus"))
earthObject = planetObjectGenerator.planet(planetaryData.getPlanetData("earth"))
marsObject = planetObjectGenerator.planet(planetaryData.getPlanetData("mars"))
jupiterObject = planetObjectGenerator.planet(planetaryData.getPlanetData("jupiter"))
saturnObject = planetObjectGenerator.planet(planetaryData.getPlanetData("saturn"))
uranusObject = planetObjectGenerator.planet(planetaryData.getPlanetData("uranus"))
neptuneObject = planetObjectGenerator.planet(planetaryData.getPlanetData("neptune"))

twoBodyProblemNew.run(earthObject, sunObject, axisLength, sphereSizeList, maxTrailLength, trailRadius, targetFrameRate, timeStep, makeVpythonPlot, makeNumPyPlot, endTime)





