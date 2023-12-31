#!/usr/bin/python3
import matplotlib.pyplot as plt
from matplotlib import animation
from math import *
import numpy as np

r = float(input(" r = "))
P = int(input("Size of primitive = "))


circumference = 360
x_points = []
y_points = []

print("Nephroid cartesian")

for s in range(0,circumference):
    x = 3 * r * cos(radians(s)) - r * cos(3 * radians(s))
    y = 3 * r * sin(radians(s)) - r * sin(3 * radians(s))
    x_points.append(x)
    y_points.append(y)

raza = plt.Line2D((0, 0), (0, 0), linewidth=0, color="k", visible=False)
circler = plt.Circle((0, 0), r, color='r', fill=False, visible=False)
circleR = plt.Circle((0, 0), 2*r, color='r', fill=False, visible=False)
punct = plt.Rectangle((0, 0), P, P, color="b", visible=True) 
plt.Circle((0, 0), float(float(P)), color="b", visible=True)
fig, ax = plt.subplots()
ax.clear()
ax.set_xlim(-1.5*3*r,1.5*3*r)
ax.set_ylim(-1.5*3*r,1.5*3*r)
trace, = ax.plot([], [], color="r")

ax.add_artist(circleR)
ax.add_artist(raza)
ax.add_artist(punct)
ax.add_artist(circler)
ax.add_artist(trace)

def init():
    circler.center = (x, y)
    punct.center = (x, y)
    ax.add_patch(circler)
    ax.add_patch(punct)
    return circler, punct,

def graphic(i):
    trace.set_data((x_points[:i], y_points[:i]))
    return trace,

def primitive(i):
    x = 3 * r * np.cos(np.radians(i))
    y = 3 * r * np.sin(np.radians(i))
    x2 = x_points[i]
    y2 = y_points[i]
    raza.set_data((x, x2), (y , y2))
    circler.center = (x, y)
    punct.set_width(P)
    punct.set_height(P)
    punct.set_xy([x2-(P/2), y2-(P/2)])
    return circler, punct, raza,

def full_animate(i):
    x = 3 * r * np.cos(np.radians(i))
    y = 3 * r * np.sin(np.radians(i))
    x2 = x_points[i]
    y2 = y_points[i]
    raza.set_data((x, x2), (y , y2))
    circler.center = (x, y)
    punct.set_width(P)
    punct.set_height(P)
    punct.set_xy([x2-(P/2), y2-(P/2)])
    trace.set_data((x_points[:i], y_points[:i]))    
    return circler, punct, raza, trace,

graphic(circumference)

anim = animation.FuncAnimation(fig, primitive,
                               init_func=init,
                               frames=circumference,
                               interval=20,
                               blit=True)
plt.grid()
plt.show()
