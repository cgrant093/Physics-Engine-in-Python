

import numpy as np

#library for plotting arrays
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

g = 9.8 # gravity
np.pi #value for pi

# Simulation Parameters, eventual inputs from user

timeSeg = 0.01 # seconds, how much time has passed between each calculation
mass = 1 # mass in unit kg

#Initalizations

#time = 0 # total time

force = np.array([0,0,-mass*g])
accel = force/mass # x, y velocity in meters/second^2
vel = np.array([1,2,3]) # x, y velocity in meters/second
pos = np.zeros(3) # x, y position in meters

#def updateForce(appForce, angle) :


def plotPos(ax, pos) :
    ax.scatter(pos[0], pos[1], pos[2], c='r')
    ax.set_zlabel("z (m)")
    ax.set_ylabel("y (m)")
    ax.set_xlabel("x (m)")
    plt.pause(0.0001)
    plt.show()

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# while loop and will stop when projectile hits to ground.
# Currently no bouncing

while pos[2] >= 0 :
    # Prints out position first
    plotPos(ax, pos)

    #
    last_accel = accel
    pos = pos + vel*timeSeg + last_accel*np.power(timeSeg, 2)/2
    new_accel = force/mass
    avg_accel = (last_accel + new_accel)/2
    vel = vel + avg_accel*timeSeg

    # Adds the time segment to the total time
    #time += timeSeg


plt.show(block=True)
