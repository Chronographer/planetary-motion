from vpython import *
import numpy as np


def run(orbitalRadiusPlanet, orbitalPeriodPlanet):
    orbitRadius = orbitalRadiusPlanet
    orbitPeriod = orbitalPeriodPlanet
    timeStep = orbitPeriod/100

    L = 5.2

    circularSpeed = (2 * np.pi * orbitRadius) / orbitPeriod
    position = vector(orbitRadius, 0, 0)
    velocity = vector(0, circularSpeed, 0)

    xAxis = curve(pos=[vector(0, 0, 0), vector(L, 0, 0)], color=vector(0.5, 0.5, 0.5))
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, L, 0)], color=vector(0.5, 0.5, 0.5))
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, L)], color=vector(0.5, 0.5, 0.5))