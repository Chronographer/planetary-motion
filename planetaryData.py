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
pretendOrbitRadius = jupiterOrbitRadius

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
pretendPeriod = jupiterPeriod

# table of masses in units of solar mass
SolarMass = 2e30
sunMass = 2.0e30 / SolarMass
mercuryMass = 2.4e23 / SolarMass
venusMass = 4.9e24 / SolarMass
earthMass = 6.0e24 / SolarMass
marsMass = 6.6e23 / SolarMass
jupiterMass = 1.9e27 / SolarMass
saturnMass = 5.7e26 / SolarMass
uranusMass = 8.8e25 / SolarMass
neptuneMass = 1.03e26 / SolarMass
plutoMass = 6.0e24 / SolarMass
pretendMass = jupiterMass

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
pretendEccentricity = jupiterEccentricity

# table of the radii of the planets (The physical size of the planet itself, NOT its orbit!) measured in Earth radii.
# these values are scaled down by a factor of 10 so that they appear as a useful size, except where otherwise noted.
# values were obtained from wikipedia https://en.wikipedia.org/wiki/List_of_Solar_System_objects_by_size on 6/10/2020
sunSphereRadius = 0.3  # The Sun is too large to be made to scale, as it would engulf the other planets.
mercurySphereRadius = 0.3829 / 10
venusSphereRadius = 0.9499 / 10
earthSphereRadius = 1 / 10
marsSphereRadius = 0.5320 / 10
jupiterSphereRadius = 10.97 / 10
saturnSphereRadius = 9.140 / 10
uranusSphereRadius = 3.981 / 10
neptuneSphereRadius = 3.865 / 10
plutoSphereRadius = 0.186 / 10
pretendSphereRadius = jupiterSphereRadius


earthPeriod = earthPeriod  # These 4 lines are temporary to easily change stuff as I am testing
earthOrbitRadius = earthOrbitRadius
pretendMass = jupiterMass * 1
earthMass = earthMass * 1


def getPlanetData(planet):
    dataList = [planet]
    if planet == "mercury":
        dataList.append(mercuryOrbitRadius)
        dataList.append(mercuryPeriod)
        dataList.append(mercuryEccentricity)
        dataList.append(mercuryMass)
        dataList.append(mercurySphereRadius)
    elif planet == "venus":
        dataList.append(venusOrbitRadius)
        dataList.append(venusPeriod)
        dataList.append(venusEccentricity)
        dataList.append(venusMass)
        dataList.append(venusSphereRadius)
    elif planet == "earth":
        dataList.append(earthOrbitRadius)
        dataList.append(earthPeriod)
        dataList.append(earthEccentricity)
        dataList.append(earthMass)
        dataList.append(earthSphereRadius)
    elif planet == "mars":
        dataList.append(marsOrbitRadius)
        dataList.append(marsPeriod)
        dataList.append(marsEccentricity)
        dataList.append(marsMass)
        dataList.append(marsSphereRadius)
    elif planet == "jupiter":
        dataList.append(jupiterOrbitRadius)
        dataList.append(jupiterPeriod)
        dataList.append(jupiterEccentricity)
        dataList.append(jupiterMass)
        dataList.append(jupiterSphereRadius)
    elif planet == "saturn":
        dataList.append(saturnOrbitRadius)
        dataList.append(saturnPeriod)
        dataList.append(saturnEccentricity)
        dataList.append(saturnMass)
        dataList.append(saturnSphereRadius)
    elif planet == "uranus":
        dataList.append(uranusOrbitRadius)
        dataList.append(uranusPeriod)
        dataList.append(uranusEccentricity)
        dataList.append(uranusMass)
        dataList.append(uranusSphereRadius)
    elif planet == "neptune":
        dataList.append(neptuneOrbitRadius)
        dataList.append(neptunePeriod)
        dataList.append(neptuneEccentricity)
        dataList.append(neptuneMass)
        dataList.append(neptuneSphereRadius)
    elif planet == "pluto":
        dataList.append(plutoOrbitRadius)
        dataList.append(plutoPeriod)
        dataList.append(plutoEccentricity)
        dataList.append(plutoMass)
        dataList.append(plutoSphereRadius)
    elif planet == "sun":
        dataList.append(sunOrbitRadius)
        dataList.append(sunPeriod)
        dataList.append(sunEccentricity)
        dataList.append(sunMass)
        dataList.append(sunSphereRadius)
    elif planet == "pretend":
        dataList.append(pretendOrbitRadius)
        dataList.append(pretendPeriod)
        dataList.append(pretendEccentricity)
        dataList.append(pretendMass)
        dataList.append(pretendSphereRadius)
    else:
        exit("Error: Could not find data for planet '" + planet + "' in  'planetaryData.py'\nPlanet object generation failed!")
    return dataList
