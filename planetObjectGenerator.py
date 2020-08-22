from vpython import vector, sphere, color, pi
traceInterval = 30  # number of time steps to wait between updating the trace. Has no effect when maxTrailLength is -2.


class makePlanet:
    def __init__(self, planetDataList, maxTrailLength):
        name = planetDataList[0]
        planetOrbitRadius = planetDataList[1]
        planetPeriod = planetDataList[2]
        eccentricity = planetDataList[3]
        mass = planetDataList[4]
        sphereRadius = planetDataList[5]

        self.name = name
        self.sphereRadius = sphereRadius
        self.mass = mass
        if self.name == 'Sun':  # this handles the sun, which is a special case as it does not have an orbital period, velocity, or eccentricity for the purposes of this lab.
            self.position = vector(0, 0, 0)
            self.velocity = vector(0, 0, 0)
            self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.yellow, make_trail=True, trail_color=color.yellow, retain=maxTrailLength, interval=traceInterval)
        else:
            # eccentricityModifier = planetOrbitRadius - (planetOrbitRadius * eccentricity)  # to include eccentricity, replace planetOrbitRadius on next line with eccentricityModifier. I do not believe this produces an accurate eccentricity, but it does make the orbit elliptical.
            initialVelocity = (2 * pi * planetOrbitRadius) / planetPeriod
            self.velocity = vector(0, initialVelocity, 0)
            self.position = vector(planetOrbitRadius, 0, 0)
            self.eccentricity = eccentricity  # currently unused value.
            self.lastPeriodEndTime = 0
            self.halfPeriodCounter = 1
            self.lastStepSign = self.velocity.y / abs(self.velocity.y)
            self.timeList = []
            self.velocityList = []
            self.positionList = []
            self.periodLengthList = []
            if self.name == 'Earth':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.blue, make_trail=True, trail_color=color.cyan, retain=maxTrailLength, interval=traceInterval)
            elif self.name == 'Mars':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.red, make_trail=True, trail_color=color.orange, retain=maxTrailLength, interval=traceInterval)
            elif self.name == 'Jupiter':
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.orange, make_trail=True, trail_color=color.red, retain=maxTrailLength, interval=traceInterval)
            else:
                self.sphere = sphere(pos=self.position, radius=self.sphereRadius, color=color.white, make_trail=True, trail_color=color.white, retain=maxTrailLength, interval=traceInterval)

        if maxTrailLength == -2:
            self.sphere.make_trail = False

    def move(self, newPosition):
        self.position = newPosition
        self.sphere.pos = self.position

    def recordTelemetry(self, currentTime):
        if self.name == 'Sun':  # The Sun's position and velocity are constant for this version of the model, so there is no point in recording its position or velocity at a given time, and thus the Sun does not have lists to store those values in as it doesnt...
            return              # ... need them, so this function does nothing if it is called for the Sun to prevent run time errors.
        self.timeList.append(currentTime)
        self.velocityList.append(self.velocity)
        self.positionList.append(self.position)

    def handlePeriodCounting(self, currentTime):
        if self.name == 'Sun':  # See comment in recordTelemetry(). (the sun has no period in this model, so there is no point in recording it)
            return
        currentStepSign = self.velocity.y / abs(self.velocity.y)
        if currentStepSign != self.lastStepSign:
            self.lastStepSign = currentStepSign
            self.halfPeriodCounter = self.halfPeriodCounter + 1
            if self.halfPeriodCounter == 2:
                self.halfPeriodCounter = 0
                currentPeriodLength = currentTime - self.lastPeriodEndTime
                self.lastPeriodEndTime = currentTime
                self.periodLengthList.append(currentPeriodLength)
