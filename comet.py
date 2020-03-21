"""
Kepler's laws demo
6/29/06
Mike Dollens Phys 685 004
edited by Antonio Cancio.
"""
from vpython import *

####Initial characteristics

GMs=4*pi**2
#group of planets=[Venus, Earth, Mars, Jupiter, Saturn, Halley's C] properties

average_distance=[0.72, 1, 1.52, 5.20, 9.54, 18]
ecc=[0.007, 0.017, 0.093, 0.048, 0.056, 0.967]
orbit_size=[]
for i in range (6):
    orbit_size=orbit_size+[average_distance[i]-ecc[i]*average_distance[i]]

mass_per_sunmass=[4.9/2e6, 6.0/2e6, .66/2e6, 1900/2e6, 570/2e6, 2e-18]
planet_size=[.04, .04, .06, .2, .2, .01]
t=0
time_step=.0001  #.01 gives large error for inner planets, and Halleys!
time_max=74

####graphics definitions

#not big enough, but oh well
sun=sphere(pos=vector(0,0,0), color=color.yellow, radius=.25)
planet_color=[color.green, color.blue, color.red, color.magenta, color.yellow, \
              color.cyan]

#grouping the definitions, setting initial char. for planets
planet_list=[]
for i in range (6):
    planet_list=planet_list+[sphere(radius=planet_size[i], \
                                    color=planet_color[i], \
                                    pos=vector(orbit_size[i],0,0))]

#Note to reader -- simplify this code!!!
for i in range (6):
    planet_list[i].vel = vector(0, sqrt(GMs)*sqrt((1+ecc[i]) \
                                                  / ((average_distance[i])*(1-ecc[i]))*(1+mass_per_sunmass[i])),0)
for i in range (6):
    planet_list[i].trail=curve(color=planet_color[i])
    scene.autoscale=0

####Euler loop

print ("Treating planet's orbits as ellipses, make demo showing Kepler's 3rd law")
print ("units are in AU")
print ("time and x coordinates as a function of time for planets")
print ("time", "venus", "earth","mars","jupiter","saturn")

while t<time_max:
    for i in range (6):
        rate
        acc=(-GMs/mag(planet_list[i].pos)**3)*planet_list[i].pos
        planet_list[i].vel=planet_list[i].vel+acc*time_step
        planet_list[i].pos=planet_list[i].pos+planet_list[i].vel*time_step
        planet_list[i].trail.append(pos=planet_list[i].pos)
    t=t+time_step

    #optional printout -- uncomment to activate)
    #mystring = ""
    #for i in range (6):
    #    mystring = mystring + str(planet_list[i].pos.x) + ","
    #    print (t,mystring)
