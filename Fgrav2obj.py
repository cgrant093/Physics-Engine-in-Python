
import math #for math.sqrt if needed
import numpy as np

#library for plotting arrays
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

np.pi # for value of pi
GConst = 6.67e-11

# def celestial bodies:

class celBody :
    def __init__(self, radius, mass, accel, vel, pos) :
        self.radius = radius
        self.mass = mass
        self.accel = accel
        self.vel = vel
        self.pos = pos

    def updateAll(self, force, timeSeg) :
        last_accel = self.accel
        last_pos = self.pos
        last_vel = self.vel

        self.pos = last_pos + last_vel*timeSeg + last_accel*np.power(timeSeg,2)/2
        new_accel = force/self.mass
        avg_accel = (last_accel + new_accel)/2
        self.vel = last_vel + avg_accel*timeSeg
        self.accel = new_accel

#def updateForce(appForce, angle) :


def plotPos(ax, b1, b2) :
    # print('sun position: ', b1.pos[0],', ', b1.pos[1],', ', b1.pos[2], '\n')
    # print('earth position: ', b2.pos[0],', ', b2.pos[1],', ', b2.pos[2], '\n')

    ax.scatter(b1.pos[0], b1.pos[1], b1.pos[2], c='y')
    ax.scatter(b2.pos[0], b2.pos[1], b2.pos[2], c='b')

    plt.pause(0.0001)
    plt.show()

def distCompSqr(b1, b2, i) :
    return (np.power(b2.pos[i]-b1.pos[i],2))

def distSqr(b1, b2) :
    return (distCompSqr(b1,b2,0) + distCompSqr(b1,b2,1) + distCompSqr(b1,b2,2))

def findAngleComp(b1, b2, i) :

    if i < 2 :
    #     xyDiag = math.sqrt(distCompSqr(b1,b2,0) + distCompSqr(b1,b2,1))
    #     theta = np.arctan2(b2.pos[1]-b1.pos[1], b2.pos[0]-b1.pos[0])

        if i == 0 :
            return ((b2.pos[0]-b1.pos[0])/math.sqrt(distSqr(b1,b2)))

        elif i == 1 :
            return ((b2.pos[1]-b1.pos[1])/math.sqrt(distSqr(b1,b2)))

        else :
            return 0

    elif i == 2 :
        return ((b2.pos[2]-b1.pos[2])/math.sqrt(distSqr(b1,b2)))

    else :
        return 0


def Fgrav2obj(b1, b2) :
    forceIntMag = GConst*b1.mass*b2.mass/distSqr(b1, b2)

    xForce = forceIntMag*findAngleComp(b1, b2, 0)
    yForce = forceIntMag*findAngleComp(b1, b2, 1)
    zForce = forceIntMag*findAngleComp(b1, b2, 2)

    Fgrav = np.array([xForce, yForce, zForce])

    return Fgrav

#def findVector(b1, b2) :
#    return np.array([b2.pos[0]-b1.pos[0], [b2.pos[1]-b1.pos[1], [b2.pos[2]-b1.pos[2]])

# Simulation Parameters, eventual inputs from user

timeSeg = 3600

#Initalizations

sun = celBody(695508e3, 1.989e30, np.zeros(3), np.zeros(3), np.zeros(3))
earth = celBody(6371e3, 5.972e24, np.zeros(3), np.array([0,30.3e3,0]), np.array([147e9,0,0]))


plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlabel("z (m)")
ax.set_ylabel("y (m)")
ax.set_xlabel("x (m)")
# while loop and will stop when projectile hits to ground.
# Currently no bouncing


k=0

while k < (365*24):
    # Prints out position first
    if k%(365*2) == 0 :
        plotPos(ax, sun, earth)

        print('sun \n ',sun.accel,'\n',sun.vel,'\n',sun.pos,'\n')
        print('earth \n ',earth.accel,'\n',earth.vel,'\n',earth.pos,'\n')

        print(k/24,'\n')
    k += 1

    forceOnSun = Fgrav2obj(sun, earth)
    forceOnEarth = -1*forceOnSun

    sun.updateAll(forceOnSun, timeSeg)
    earth.updateAll(forceOnEarth, timeSeg)



    # Adds the time segment to the total time
    #time += timeSeg


plt.show(block=True)
