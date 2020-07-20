from vpython import vector, sphere, color
import numpy as np
traceInterval = 10  # number of time steps to wait between updating the trace. Has no effect when maxTrailLength is -2.


class makePlanet:
    def __init__(self, planetDataList, maxTrailLength, planetObjectList):
        name = planetDataList[0]
        planetOrbitRadius = planetDataList[1]
        planetPeriod = planetDataList[2]
        eccentricity = planetDataList[3]
        mass = planetDataList[4]
        sphereRadius = planetDataList[5]

        self.name = name
        self.sphereRadius = sphereRadius
        self.mass = mass
        self.momentum = 0  # This is a placeholder value
        if self.name != 'sun':
            # eccentricityModifier = planetOrbitRadius - (planetOrbitRadius * eccentricity)  # to include eccentricity, replace planetOrbitRadius on next line with eccentricityModifier. I do not believe this produces an accurate eccentricity, but it does make the orbit elliptical.
            initialVelocity = (2 * np.pi * planetOrbitRadius) / planetPeriod
            self.velocity = vector(0, initialVelocity, 0)
            self.position = vector(planetOrbitRadius, 0, 0)
            self.momentum = self.mass * np.norm(self.velocity)
            self.eccentricity = eccentricity  # currently unused value.
            if self.name == 'earth':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.blue, make_trail=True, trail_color=color.cyan, retain=maxTrailLength, interval=traceInterval)
            elif self.name == 'mars':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.red, make_trail=True, trail_color=color.orange, retain=maxTrailLength, interval=traceInterval)
            elif self.name == 'jupiter':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.orange, make_trail=True, trail_color=color.red, retain=maxTrailLength, interval=traceInterval)
            else:
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.white, make_trail=True, trail_color=color.white, retain=maxTrailLength, interval=traceInterval)

            if maxTrailLength == -2:
                self.sphere.make_trail = False
        else:
            for planet in range(0, len(planetObjectList-1)):
                self.momentum = self.momentum + planet.momentum
            self.momentum = -self.momentum
            self.position = vector(0, 0, 0)
            self.velocity = vector(0, 0, 0)
            self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.yellow)


    def move(self, newPosition):
        self.position = newPosition
        self.sphere.pos = self.position
