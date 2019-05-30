"""
Pyscho py example script to work through its various functionalities.
Pyschopy has various modules like visual and event that contain relevant
functionality for running experiments.
"""
from psychopy import visual, event

#Creates window object with desired size/color.
win = visual.Window(
	size = [400, 400],
	color = [1, 1, 1],
	units = "pix",
	fullscr = False)

#Creates a text stimulus in the window with black color
text = visual.TextStim(win = win, text="Hello World", color = [-1, -1, -1])
#Draws the text stim on screen, all stimuli have this method.
text.draw()

#renders the stimuli that have been drawn and clears all previous stimuli
win.flip()

#Halts program execution until a key is pressed.
event.waitKeys()

line = visual.Line(win = win, units = "pix", lineColor = [-1, -1, -1],
	start = [-200, -200], end = [200, 200])

line.draw()

#re renders the window, wiping the previous stimuli
win.flip()

event.waitKeys()

circ = visual.Circle(
	win=win,
    units="pix",
    radius=150,
    fillColor=[0, 0, 0],
    lineColor=[-1, -1, -1],
    edges=128)

circ.draw()
win.flip()

event.waitKeys()

img = visual.ImageStim(
	win = win,
	image = "machine.jpg")

img.draw()
win.flip()
event.waitKeys()
#closes the window.s
win.close()