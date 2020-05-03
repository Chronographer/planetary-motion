from vpython import vector
import numpy as np


class planet:
    def __init__(self, planetDataList):
        planetOrbitRadius = planetDataList[0]
        planetPeriod = planetDataList[1]
        eccentricity = planetDataList[2]
        mass = planetDataList[3]

        if planetOrbitRadius == "Null":  # this handles the sun, which is a special case as it does not have an orbital period, velocity, or eccentricity for the purposes of this lab.
            self.position = vector(0, 0, 0)
            self.mass = mass
            self.velocity = vector(0, 0, 0)
        else:
            eccentricityModifier = planetOrbitRadius - (planetOrbitRadius * eccentricity)
            initialVelocity = (2 * np.pi * planetOrbitRadius) / planetPeriod
            self.velocity = vector(0, initialVelocity, 0)
            self.position = vector(planetOrbitRadius, 0, 0)
            self.eccentricity = eccentricity
            self.mass = mass
