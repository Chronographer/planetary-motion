import twoBodyProblem
import planetaryData
import numpy as np
from vpython import *

title = "test scene"
scene = canvas(title=title, width=640, height=480, forward=vector(-1, -1, -1))
timeStep = planetaryData.earthPeriod / 100
maxTrailLength = 70  # To remove the limit set this to -1, to remove the trail entirely, set this to -2

twoBodyProblem.run(planetaryData.earthOrbitRadius, planetaryData.earthPeriod, maxTrailLength, timeStep)
