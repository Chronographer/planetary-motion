from vpython import vector
import numpy as np


class planet:
    def __init__(self, planetDataList):
        name = planetDataList[0]
        planetOrbitRadius = planetDataList[1]
        planetPeriod = planetDataList[2]
        eccentricity = planetDataList[3]
        mass = planetDataList[4]
        sphereRadius = planetDataList[5]

        self.name = name
        self.sphereRadius = sphereRadius
        if planetOrbitRadius == "Null":  # this handles the sun, which is a special case as it does not have an orbital period, velocity, or eccentricity for the purposes of this lab.
            self.position = vector(0, 0, 0)
            self.mass = mass
            self.velocity = vector(0, 0, 0)
        else:
            eccentricityModifier = planetOrbitRadius - (planetOrbitRadius * eccentricity)  # to include eccentricity, replace planetOrbitRadius on next line with eccentricityModifier.
            initialVelocity = (2 * np.pi * planetOrbitRadius) / planetPeriod
            self.velocity = vector(0, initialVelocity, 0)
            self.position = vector(planetOrbitRadius, 0, 0)
            self.eccentricity = eccentricity
            self.mass = mass
