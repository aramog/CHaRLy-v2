from psychopy import visual, event

from taskHelpers import *

#Helpers for printing tutorial text:
def instructionsScreen(win):
	"""Shows the instruction screen for the start
	of the trial."""
	header = visual.TextStim(
		win = win,
		text = "Press any key to move on.",
		pos = [0, 250],
		color = [-1, -1, -1],
		height = 30)
	header.draw()

	firstBulletText = "Your objective is to as earn as many points as possible by unlocking stars. Stars are unlocked using a machine which is controlled by the D, F, J, and K keys. Each star is unlocked by a unique sequence of four key presses."

	firstBullet = visual.TextStim(
		win = win,
		text = firstBulletText,
		pos = [0, 0],
		color = [-1, -1, -1],
		height = 30)
	firstBullet.draw()
	win.flip()
	event.waitKeys()

	header.draw()

	secondBulletText = "The machine’s inner workings will sometimes be visible to you, and you should use this information to help you unlock more stars."
	secondBullet = visual.TextStim(
		win = win,
		text = secondBulletText,
		pos = [0, 0],
		color = [-1, -1, -1],
		height = 30)
	secondBullet.draw()

	win.flip()
	event.waitKeys()

	header.draw()

	thirdBulletText = "Every trial, we will highlight the star you should try to unlock. Only this star will give you points. You can still unlock the other star, but you won't earn any points."
	thirdBullet = visual.TextStim(
		win = win,
		text = thirdBulletText,
		pos = [0, 0],
		color = [-1, -1, -1],
		height = 30)
	thirdBullet.draw()

	win.flip()
	event.waitKeys()

	pressKeyText = "Press any key to start an interactive tutorial!"
	pressKey = visual.TextStim(
		win = win,
		text = pressKeyText,
		pos = [0, 0],
		color = [-1, -1, -1],
		height = 40)
	pressKey.draw()

def tutorial1Text(win):
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

def tutorial2Text(win):
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

def tutorial3Text(win):
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

def tutorial4Text(win):
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

def tutorial5Text(win):
	"""Shows the text instructions for the fifth screen
	of the tutorial."""
	text = "You’ve made a star appear to earn 100 points! \n \n Notice that a star is unlocked when you form some sequence of the machine's components."
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [-500, 0],
		color = [-1, -1, -1],
		height = 30,
		wrapWidth = 350)
	textStim.draw()

def readyToPlayScreen(win):
	"""Shows the last screen of the tutorial phase,
	asking participants if they are reading to begin."""
	text = "Press any key when you're ready to start the game!"
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 0],
		color = [-1, -1, -1],
		height = 40)
	textStim.draw()

def runTutorial(win):
	instructionsScreen(win)
	win.flip()
	event.waitKeys()

	drawBlankTask(win)
	highlightStar(win, "assets/black-star.png")
	pointCounter(win, 0)
	tutorial1Text(win)
	win.flip()
	event.waitKeys(keyList = ["d"])

	drawBlankTask(win)
	highlightStar(win, "assets/black-star.png")
	pointCounter(win, 0)
	showKeys(win, ["d"])
	tutorial2Text(win)
	win.flip()
	event.waitKeys(keyList = ["k"])

	drawBlankTask(win)
	highlightStar(win, "assets/black-star.png")
	drawGear(win, 0)
	pointCounter(win, 0)
	showKeys(win, ["d", "k"])
	tutorial3Text(win)
	win.flip()
	event.waitKeys(keyList = ["j"])

	drawBlankTask(win)
	highlightStar(win, "assets/black-star.png")
	drawGear(win, 0)
	pointCounter(win, 0)
	showKeys(win, ["d", "k", "j"])
	tutorial4Text(win)
	win.flip()
	event.waitKeys(keyList = ["f"])


	drawBlankTask(win)
	highlightAndUnlock(win, "assets/black-star.png")
	unlockStar(win, "assets/black-star.png")
	drawGear(win, 0)
	drawLight(win, 1)
	pointCounter(win, 100)
	showKeys(win, ["d", "k", "j", "f"])
	tutorial5Text(win)
	win.flip()
	event.waitKeys()

	readyToPlayScreen(win)
	win.flip()
	event.waitKeys()
	