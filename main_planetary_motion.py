import twoBodyProblem
import numpy as np
from vpython import *

title = "test scene"
L = 5.2
scene = canvas(title=title, width=640, height=480, range=2*L, forward=vector(-1, -1, -1))

twoBodyProblem.run(1, 2 * np.pi)
