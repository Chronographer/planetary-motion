from vpython import vector, sphere, color, pi
import planetaryData

""" Script to generate planet objects. ONLY use with 'trueThreeBodyProblem.py'. For all other scripts, use 'planetObjectGenerator.py'. """

traceInterval = 30  # number of time steps to wait between updating the trace. Has no effect when maxTrailLength is -2.


def generatePlanetList(planetList, maxTrailLength):
    planetObjectList = []
    for i in range(len(planetList)):
        planetDataList = planetaryData.getPlanetData(planetList[i])
        planetObject = makePlanet(planetDataList, maxTrailLength, planetObjectList)
        planetObjectList.append(planetObject)
    return planetObjectList


class makePlanet:
    def __init__(self, planetDataList, maxTrailLength, planetObjectList):
        name = planetDataList[0]
        planetOrbitRadius = planetDataList[1]
        planetPeriod = planetDataList[2]
        # eccentricity = planetDataList[3]
        mass = planetDataList[4]
        sphereRadius = planetDataList[5]

        self.name = name
        self.sphereRadius = sphereRadius
        self.mass = mass
        self.timeList = []
        self.positionList = []
        self.velocityList = []
        if self.name != 'sun':
            # eccentricityModifier = planetOrbitRadius - (planetOrbitRadius * eccentricity)  # to include eccentricity, replace planetOrbitRadius on next line with eccentricityModifier. I do not believe this produces an accurate eccentricity, but it does make the orbit elliptical.
            initialVelocity = (2 * pi * planetOrbitRadius) / planetPeriod
            self.velocity = vector(0, initialVelocity, 0)
            self.position = vector(planetOrbitRadius, 0, 0)

            if self.name == 'earth':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.blue, make_trail=True, trail_color=color.cyan, retain=maxTrailLength, interval=traceInterval)
            elif self.name == 'mars':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.red, make_trail=True, trail_color=color.orange, retain=maxTrailLength, interval=traceInterval)
            elif self.name == 'jupiter':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.orange, make_trail=True, trail_color=color.red, retain=maxTrailLength, interval=traceInterval)
            else:
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.white, make_trail=True, trail_color=color.white, retain=maxTrailLength, interval=traceInterval)
        else:
            totalPlanetMomentum = vector(0, 0, 0)
            positionOffsetThing = 0
            for index in range(len(planetObjectList)):
                planet = planetObjectList[index]
                totalPlanetMomentum = totalPlanetMomentum + (planet.mass * planet.velocity)
                positionOffsetThing = positionOffsetThing + (planet.mass * planet.position.x)
            sunPositionOffset = -positionOffsetThing / self.mass
            self.velocity = -totalPlanetMomentum / self.mass
            self.position = vector(sunPositionOffset, 0, 0)
            self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.yellow, make_trail=True, trail_color=color.yellow, retain=maxTrailLength, interval=traceInterval)

        if maxTrailLength == -2:
            self.sphere.make_trail = False

    def move(self, newPosition):
        self.position = newPosition
        self.sphere.pos = self.position

    def recordTelemetry(self, currentTime):
        self.timeList.append(currentTime)
        self.velocityList.append(self.velocity)
        self.positionList.append(self.position)
