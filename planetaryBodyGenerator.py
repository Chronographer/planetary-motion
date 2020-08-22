from vpython import vector, sphere, color, pi
import planetaryData

"""
Script to generate planet objects. ONLY use with models which assume a dynamically modeled Sun, or you will have problems. 
For all other models, use 'planetObjectGenerator.py'.
"""

traceInterval = 30  # number of time steps to wait between updating the trace. Has no effect when maxTrailLength is -2.


def generatePlanetList(planetList, maxTrailLength):
    planetObjectList = []
    for i in range(len(planetList)):
        planetDataList = planetaryData.getPlanetData(planetList[i])
        planetObject = planet(planetDataList, maxTrailLength, planetObjectList)
        planetObjectList.append(planetObject)
    return planetObjectList


class planet:
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
        self.lastPeriodEndTime = 0
        self.halfPeriodCounter = 1
        self.timeList = []
        self.positionList = []
        self.velocityList = []
        self.periodLengthList = []
        if self.name != 'Sun':
            # eccentricityModifier = planetOrbitRadius - (planetOrbitRadius * eccentricity)  # to include eccentricity, replace planetOrbitRadius on next line with eccentricityModifier. I do not believe this produces an accurate eccentricity, but it does make the orbit elliptical.
            initialVelocity = (2 * pi * planetOrbitRadius) / planetPeriod
            self.velocity = vector(0, initialVelocity, 0)
            self.position = vector(planetOrbitRadius, 0, 0)

            if self.name == 'Earth':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.blue, make_trail=True, trail_color=color.cyan, retain=maxTrailLength, interval=traceInterval)
            elif self.name == 'Mars':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.red, make_trail=True, trail_color=color.orange, retain=maxTrailLength, interval=traceInterval)
            elif self.name == 'Jupiter':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.orange, make_trail=True, trail_color=color.red, retain=maxTrailLength, interval=traceInterval)
            elif self.name == 'Uranus':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.blue, make_trail=True, trail_color=color.cyan, retain=maxTrailLength, interVal=traceInterval)
            else:
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.white, make_trail=True, trail_color=color.white, retain=maxTrailLength, interval=traceInterval)
        else:
            totalPlanetMomentum = vector(0, 0, 0)
            positionOffsetThing = 0
            for index in range(len(planetObjectList)):
                localPlanet = planetObjectList[index]
                totalPlanetMomentum = totalPlanetMomentum + (localPlanet.mass * localPlanet.velocity)
                positionOffsetThing = positionOffsetThing + (localPlanet.mass * localPlanet.position.x)
            sunPositionOffset = -positionOffsetThing / self.mass
            self.velocity = -totalPlanetMomentum / self.mass
            self.position = vector(sunPositionOffset, 0, 0)
            self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.yellow, make_trail=True, trail_color=color.yellow, retain=maxTrailLength, interval=traceInterval)
        self.lastStepSign = self.velocity.y / abs(self.velocity.y)

        if maxTrailLength == -2:
            self.sphere.make_trail = False

    def move(self, newPosition):
        self.position = newPosition
        self.sphere.pos = self.position

    def recordTelemetry(self, currentTime):
        self.timeList.append(currentTime)
        self.velocityList.append(self.velocity)
        self.positionList.append(self.position)

    def handlePeriodCounting(self, currentTime):
        currentStepSign = self.velocity.y / abs(self.velocity.y)
        if currentStepSign != self.lastStepSign:
            self.lastStepSign = currentStepSign
            self.halfPeriodCounter = self.halfPeriodCounter + 1
            if self.halfPeriodCounter == 2:
                self.halfPeriodCounter = 0
                currentPeriodLength = currentTime - self.lastPeriodEndTime
                self.lastPeriodEndTime = currentTime
                self.periodLengthList.append(currentPeriodLength)
