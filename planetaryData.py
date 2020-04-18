# table of orbital radii in AU
sunOrbitRadius = "Null"
mercuryOrbitRadius = 0.39
venusOrbitRadius = 0.72
earthOrbitRadius = 1.001
marsOrbitRadius = 1.52
jupiterOrbitRadius = 5.20
saturnOrbitRadius = 9.54
uranusOrbitRadius = 19.19
neptuneOrbitRadius = 30.06
plutoOrbitRadius = 39.53
pretendOrbitRadius = 3.21

# table of orbital periods in years
sunPeriod = "Null"
mercuryPeriod = 0.240846
venusPeriod = 0.615
earthPeriod = 1.00
marsPeriod = 1.881
jupiterPeriod = 11.86
saturnPeriod = 29.46
uranusPeriod = 84.01
neptunePeriod = 164.8
plutoPeriod = 248.1
pretendPeriod = 5.1

# table of masses in units of solar mass
SolarMass = 2e30
sunMass = 2.0e30 / SolarMass
mercuryMass = 2.4e23 / SolarMass
venusMass = 4.9e24 / SolarMass
earthMass = 6.0e24 / SolarMass
marsMass = 6.6e23 / SolarMass
jupiterMass = 1.9e27 / SolarMass  # jupiter's real mass is 1.9e27
saturnMass = 5.7e26 / SolarMass
uranusMass = 8.8e25 / SolarMass
neptuneMass = 1.03e26 / SolarMass
plutoMass = 6.0e24 / SolarMass
pretendMass = 6.6e23 / SolarMass

# table of eccentricities of the planets
sunEccentricity = "Null"
mercuryEccentricity = 0.206
venusEccentricity = 0.007
earthEccentricity = 0.017
marsEccentricity = 0.093
jupiterEccentricity = 0.048
saturnEccentricity = 0.056
uranusEccentricity = 0.046
neptuneEccentricity = 0.010
plutoEccentricity = 0.248
pretendEccentricity = 0.031


def getPlanetData(planet):
    dataList = []
    if planet == "mercury":
        dataList.append(mercuryOrbitRadius)
        dataList.append(mercuryPeriod)
        dataList.append(mercuryEccentricity)
        dataList.append(mercuryMass)
    elif planet == "venus":
        dataList.append(venusOrbitRadius)
        dataList.append(venusPeriod)
        dataList.append(venusEccentricity)
        dataList.append(venusMass)
    elif planet == "earth":
        dataList.append(earthOrbitRadius)
        dataList.append(earthPeriod)
        dataList.append(earthEccentricity)
        dataList.append(earthMass)
    elif planet == "mars":
        dataList.append(marsOrbitRadius)
        dataList.append(marsPeriod)
        dataList.append(marsEccentricity)
        dataList.append(marsMass)
    elif planet == "jupiter":
        dataList.append(jupiterOrbitRadius)
        dataList.append(jupiterPeriod)
        dataList.append(jupiterEccentricity)
        dataList.append(jupiterMass)
    elif planet == "saturn":
        dataList.append(saturnOrbitRadius)
        dataList.append(saturnPeriod)
        dataList.append(saturnEccentricity)
        dataList.append(saturnMass)
    elif planet == "uranus":
        dataList.append(uranusOrbitRadius)
        dataList.append(uranusPeriod)
        dataList.append(uranusEccentricity)
        dataList.append(uranusMass)
    elif planet == "neptune":
        dataList.append(neptuneOrbitRadius)
        dataList.append(neptunePeriod)
        dataList.append(neptuneEccentricity)
        dataList.append(neptuneMass)
    elif planet == "pluto":
        dataList.append(plutoOrbitRadius)
        dataList.append(plutoPeriod)
        dataList.append(plutoEccentricity)
        dataList.append(plutoMass)
    elif planet == "sun":
        dataList.append(sunOrbitRadius)
        dataList.append(sunPeriod)
        dataList.append(sunEccentricity)
        dataList.append(sunMass)
    elif planet == "pretend":
        dataList.append(pretendOrbitRadius)
        dataList.append(pretendPeriod)
        dataList.append(pretendEccentricity)
        dataList.append(pretendMass)
    return dataList
