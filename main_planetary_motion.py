import twoBodyProblem
import planetaryData
import numpy as np
from vpython import *

title = "test scene"
scene = canvas(title=title, width=640, height=480, forward=vector(-1, -1, -1))
timeStep = 0.01

twoBodyProblem.run(planetaryData.earthOrbitRadius, planetaryData.earthPeriod, timeStep)
