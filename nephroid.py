#!/usr/bin/python3
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
from matplotlib import animation
from math import *
import numpy as np

def cartesian():
	global canvas
	if canvas:
	    canvas.get_tk_widget().destroy()	

	r = graphicSize.get() #Радиус малой окружности. В нефроиде малая окружность в 2 раза меньше большей.
	P = primitiveSize.get()

	text1.set("Размера примитива:")

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
	punct = plt.Rectangle((0, 0), P, P, color="b", visible=Var1.get()) 
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

	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.draw()

	toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
	toolbar.update()

	canvas.mpl_connect(
	    "key_press_event", lambda event: print(f"you pressed {event.key}"))
	canvas.mpl_connect("key_press_event", key_press_handler)

	canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

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
	root.mainloop()

def polar():
	global canvas
	if canvas:
	    canvas.get_tk_widget().destroy()

	a = graphicSize.get()
	P = primitiveSize.get()

	text1.set("Размера примитива:")

	theta = np.pi * 2
	rads = np.arange(0, (theta), 0.01)
	circumference = len(rads)
	r_points = []

	print("Nephroid polar")

	for rad in rads:
	    r = np.sqrt(2) * a * pow(( pow(1-np.cos(rad), 1/3) + pow(np.cos(rad) + 1, 1/3) ), 3/2)
	    r_points.append(r)

	punct = plt.Rectangle((0, 0), P, P, color="b", visible=Var1.get())
	fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
	trace, = ax.plot([], [], color="r")
	ax.grid(True)
	ax.add_artist(punct)
	ax.add_artist(trace)

	ax.set_rmax(4.2*a)

	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.draw()

	toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
	toolbar.update()

	canvas.mpl_connect(
	    "key_press_event", lambda event: print(f"you pressed {event.key}"))
	canvas.mpl_connect("key_press_event", key_press_handler)

	canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

	def init():
	    ax.add_patch(punct)
	    return punct,

	def graphic(i):
	    trace.set_data((rads[:i], r_points[:i]))
	    return trace,

	def primitive(i):
	    x2 = rads[i]
	    y2 = r_points[i]
	    punct.set_width(P/(4*a))
	    punct.set_height(P)
	    punct.set_xy([x2-(P/(8*a)), y2-(P/2)])
	    return punct,

	graphic(circumference)
	anim = animation.FuncAnimation(fig, primitive,
	                               init_func=init,
	                               frames=circumference,
	                               interval=20,
	                               blit=True)
	tkinter.mainloop()

root = tkinter.Tk()

button_c = tkinter.Button(master=root, text="Обновить график\n(в декартовой системе координат)", command=cartesian)
button_c.pack(side=tkinter.BOTTOM)
button_p = tkinter.Button(master=root, text="Обновить график\n(в полярной системе координат)", command=polar)
button_p.pack(side=tkinter.BOTTOM)

canvas = None

Var1 = tkinter.IntVar()
c1 = tkinter.Checkbutton(root, text='Примитив',variable=Var1, onvalue=1)
c1.pack(side=tkinter.TOP)

text1 = tkinter.StringVar()
text1.set("Размера примитива:")
label1 = tkinter.Label( root, textvariable=text1)
label1.pack(side=tkinter.TOP)
primitiveSize = tkinter.IntVar()
entry_primitive = tkinter.Entry( root, textvariable=primitiveSize)
primitiveSize.set("2")
entry_primitive.pack(side=tkinter.TOP)

text2 = tkinter.StringVar()
text2.set("Размера графика (радиус):")
label2 = tkinter.Label( root, textvariable=text2)
label2.pack(side=tkinter.TOP)
graphicSize = tkinter.IntVar()
entry_graphic = tkinter.Entry( root, textvariable=graphicSize)
graphicSize.set("16")
entry_graphic.pack(side=tkinter.TOP)

root.mainloop()
