"""
The tutorial is organized by the screens that the user sees:
screen1: Goal is to collect stars
screen2: Machince is how you make those stars
screen3: Interact with machine to produce smoke
screen4: Interact with machine to produce star
screen5: Questions?

runTutorial: main function that runs all screens in the
correct order

The only argument for all functions is the window to draw.
"""

from psychopy import visual, event

from taskHelpers import *


def screen1(win):
	text = "Your goal in this task is to earn points by unlocking stars"
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 150],
		color = [-1, -1, -1],
		height = 50)
	textStim.draw()

	blueStar = visual.ImageStim(
		win = win,
		image = "assets/blue-star.png",
		pos = [-200, -75])
	blueStar.draw()
	
	orangeStar = visual.ImageStim(
		win = win,
		image = "assets/orange-star.png",
		pos = [-65, -200])
	orangeStar.draw()

	blackStar = visual.ImageStim(
		win = win,
		image = "assets/black-star.png",
		pos = [65, -75])
	blackStar.draw()

	grayStar = visual.ImageStim(
		win = win,
		image = "assets/gray-star.png",
		pos = [200, -200])
	grayStar.draw()

	win.flip()
	event.waitKeys()

def screen2(win):
	text = "This machine can make stars"
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 250],
		color = [-1, -1, -1],
		height = 40)
	textStim.draw()

	machine = visual.ImageStim(
		win = win,
		image = "assets/machine.jpg",
		pos = [0, 0])
	machine.draw()
	win.flip()
	event.waitKeys()

	text2 = "You can control the machine using the D, F, J, and K keys"
	textStim2 = visual.TextStim(
		win = win,
		text = text2,
		pos = [0, -260],
		color = [-1, -1, -1],
		height = 40)
	textStim2.draw()
	machine.draw()
	textStim.draw()
	win.flip()
	event.waitKeys()

def screen3(win):
	text = "Try out using the machine yourself!"
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 250],
		color = [-1, -1, -1],
		height = 40)
	textStim.draw()

	keyPresses = []

	drawBlankTask(win)
	win.flip()
	keyPresses.append(getKeys())

	textStim.draw()
	drawBlankTask(win)
	showKeys(win, keyPresses)
	win.flip()
	keyPresses.append(getKeys())
	
	textStim.draw()
	drawBlankTask(win)
	showKeys(win, keyPresses)
	win.flip()
	keyPresses.append(getKeys())

	textStim.draw()
	drawBlankTask(win)
	showKeys(win, keyPresses)
	win.flip()
	keyPresses.append(getKeys())

	textStim.draw()
	drawBlankTask(win)
	showKeys(win, keyPresses)
	unlockStar(win, "assets/smoke.png")
	win.flip()
	event.waitKeys()

def screen4(win):
	def screen4Text1(win):
		"""Shows the text instructions for the first screen
		of the tutorial."""
		text = "To start, try pressing the D key."
		textStim = visual.TextStim(
			win = win,
			text = text,
			pos = [-500, 0],
			color = [-1, -1, -1],
			height = 30,
			wrapWidth = 275)
		textStim.draw()

	def screen4Text2(win):
		"""Shows the text instructions for the second screen
		of the tutorial."""
		text = "Nothing has happened yet, but remember that you need to use sequences of actions to unlock items. \n\n Try pressing K."
		textStim = visual.TextStim(
			win = win,
			text = text,
			pos = [-500, 0],
			color = [-1, -1, -1],
			height = 30,
			wrapWidth = 350)
		textStim.draw()

	def screen4Text3(win):
		"""Shows the text instructions for the third screen
		of the tutorial."""
		text = "You’ve made a gear appear with the key combination DK! The machine will use these parts to create stars. \n \n Now try pressing J"
		textStim = visual.TextStim(
			win = win,
			text = text,
			pos = [-500, 0],
			color = [-1, -1, -1],
			height = 30,
			wrapWidth = 350)
		textStim.draw()

	def screen4Text4(win):
		"""Shows the text instructions for the fourth screen
		of the tutorial."""
		text = "Now try pressing F."
		textStim = visual.TextStim(
			win = win,
			text = text,
			pos = [-500, 0],
			color = [-1, -1, -1],
			height = 30,
			wrapWidth = 350)
		textStim.draw()

	def screen4Text5(win):
		"""Shows the text instructions for the fifth screen
		of the tutorial."""
		text = "You’ve made a star appear to earn 100 points! \n \n Notice that a star is unlocked when you form some sequence of the machine's parts."
		textStim = visual.TextStim(
			win = win,
			text = text,
			pos = [-500, 0],
			color = [-1, -1, -1],
			height = 30,
			wrapWidth = 350)
		textStim.draw()
	
	text = "Unlocking stars can be hard! Luckily for you, this machine has a window so you can see how it works."
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 250],
		color = [-1, -1, -1],
		height = 30)
	textStim.draw()

	drawBlankTask(win)
	screen4Text1(win)
	win.flip()
	event.waitKeys(keyList = ["d"])

	textStim.draw()
	drawBlankTask(win)
	showKeys(win, ["d"])
	screen4Text2(win)
	win.flip()
	event.waitKeys(keyList = ["k"])

	textStim.draw()
	drawBlankTask(win)
	drawGear(win, 0)
	showKeys(win, ["d", "k"])
	screen4Text3(win)
	win.flip()
	event.waitKeys(keyList = ["j"])

	textStim.draw()
	drawBlankTask(win)
	drawGear(win, 0)
	showKeys(win, ["d", "k", "j"])
	screen4Text4(win)
	win.flip()
	event.waitKeys(keyList = ["f"])

	textStim.draw()
	drawBlankTask(win)
	unlockStar(win, "assets/black-star.png")
	drawGear(win, 0)
	drawLight(win, 1)
	showKeys(win, ["d", "k", "j", "f"])
	screen4Text5(win)
	win.flip()
	event.waitKeys()

def screen5(win):
	text = "Do you have any questions?"
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 150],
		color = [-1, -1, -1],
		height = 50)
	textStim.draw()

	text2 = "Once you're ready to start, press any key to begin!"
	textStim2 = visual.TextStim(
		win = win,
		text = text2,
		pos = [0, -200],
		color = [-1, -1, -1],
		height = 50)
	textStim2.draw()

	win.flip()
	event.waitKeys()

def runTutorial(win):
	screen1(win)
	screen2(win)
	screen3(win)
	screen4(win)
	screen5(win)
