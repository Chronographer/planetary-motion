from vpython import *
import numpy as np


def run(earth, jupiter, axisLength, sphereSizeList, maxTrailLength, trailRadius):
    xAxis = curve(pos=[vector(0, 0, 0), vector(axisLength, 0, 0)], color=color.red)
    yAxis = curve(pos=[vector(0, 0, 0), vector(0, axisLength, 0)], color=color.green)
    zAxis = curve(pos=[vector(0, 0, 0), vector(0, 0, axisLength)], color=color.blue)
    sunSphere = sphere(pos=vector(0, 0, 0), radius=sphereSizeList[0], color=color.yellow)
    earthSphere = sphere(pos=earth.position, radius=sphereSizeList[1], color=color.cyan)
    jupiterSphere = sphere(pos=jupiter.position, radius=sphereSizeList[2], color=color.orange)
    if maxTrailLength != -2:
        earthSphere.trail = curve(pos=[earth.pos], color=color.blue, radius=trailRadius, retain=maxTrailLength, interval=30)
        jupiterSphere.trail = curve(pos=[earth.pos], color=color.blue, radius=trailRadius, retain=maxTrailLength, interval=30)



