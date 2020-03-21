# table of orbital radii in AU
mercuryOrbitRadius = 0.39
venusOrbitRadius = 0.72
earthOrbitRadius = 1.001
marsOrbitRadius = 1.52
jupiterOrbitRadius = 5.20
saturnOrbitRadius = 9.54
uranusOrbitRadius = 19.19
neptuneOrbitRadius = 30.06
plutoOrbitRadius = 39.53

# table of orbital periods in years
mercuryPeriod = 0.240846
venusPeriod = 0.615
earthPeriod = 1.00
marsPeriod = 1.881
jupiterPeriod = 11.86
saturnPeriod = 29.46
uranusPeriod = 84.01
neptunePeriod = 164.8
plutoPeriod = 248.1

# table of masses in units of solar mass
SolarMass = 2e30
massSun = 2.0e30 / SolarMass
massMercury = 2.4e23 / SolarMass
massVenus = 4.9e24 / SolarMass
massEarth = 6.0e24 / SolarMass
massMars = 6.6e23 / SolarMass
massJupiter = 1.9e27 / SolarMass
massSaturn = 5.7e26 / SolarMass
massUranus = 8.8e25 / SolarMass
massNeptune = 1.03e26 / SolarMass
massPluto = 6.0e24 / SolarMass

# table of eccentricities of the planets
mercuryEccentricity = 0.206
venusEccentricity = 0.007
earthEccentricity = 0.017
marsEccentricity = 0.093
jupiterEccentricity = 0.048
saturnEccentricity = 0.056
uranusEccentricity = 0.046
neptuneEccentricity = 0.010
plutoEccentricity = 0.248


def getPlanetData(planet):
    dataList = []
    if planet == "mercury":
        dataList.append(mercuryOrbitRadius)
        dataList.append(mercuryPeriod)
        dataList.append(mercuryEccentricity)
    elif planet == "venus":
        dataList.append(venusOrbitRadius)
        dataList.append(venusPeriod)
        dataList.append(venusEccentricity)
    elif planet == "earth":
        dataList.append(earthOrbitRadius)
        dataList.append(earthPeriod)
        dataList.append(earthEccentricity)
    elif planet == "mars":
        dataList.append(marsOrbitRadius)
        dataList.append(marsPeriod)
        dataList.append(marsEccentricity)
    elif planet == "jupiter":
        dataList.append(jupiterOrbitRadius)
        dataList.append(jupiterPeriod)
        dataList.append(jupiterEccentricity)
    elif planet == "saturn":
        dataList.append(saturnOrbitRadius)
        dataList.append(saturnPeriod)
        dataList.append(saturnEccentricity)
    elif planet == "uranus":
        dataList.append(uranusOrbitRadius)
        dataList.append(uranusPeriod)
        dataList.append(uranusEccentricity)
    elif planet == "neptune":
        dataList.append(neptuneOrbitRadius)
        dataList.append(neptunePeriod)
        dataList.append(neptuneEccentricity)
    elif planet == "pluto":
        dataList.append(plutoOrbitRadius)
        dataList.append(plutoPeriod)
        dataList.append(plutoEccentricity)
    return dataList
