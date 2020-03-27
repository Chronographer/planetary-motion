from vpython import vector
import numpy as np


class planet:
    def __init__(self, planetDataList):
        planetOrbitRadius = planetDataList[0]
        planetPeriod = planetDataList[1]
        eccentricity = planetDataList[2]

        initialVelocity = (2 * np.pi * planetOrbitRadius) / planetPeriod
        self.velocity = vector(0, initialVelocity, 0)
        self.position = vector(planetOrbitRadius, 0, 0)
        self.eccentricity = eccentricity
