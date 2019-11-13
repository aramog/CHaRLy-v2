"""
The tutorial is organized by the screens that the user sees:
screen1: Goal is to collect coins
screen2: Machince is how you make those coins
screen3: Interact with machine to produce smoke
screen4: Interact with machine to produce coin
screen5: Questions?

runTutorial: main function that runs all screens in the
correct order

The only argument for all functions is the window to draw.
"""

from psychopy import visual, event

from taskHelpers import *


def screen1(win):
	text = "Your goal in this task is to earn points by unlocking coins."
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 150],
		color = [-1, -1, -1],
		height = 50)
	textStim.draw()

	bluecoin = visual.ImageStim(
		win = win,
		image = "assets/tutorial/coin.png",
		pos = [-200, -75])
	bluecoin.draw()
	
	orangecoin = visual.ImageStim(
		win = win,
		image = "assets/tutorial/coin.png",
		pos = [-65, -200])
	orangecoin.draw()

	blackcoin = visual.ImageStim(
		win = win,
		image = "assets/tutorial/coin.png",
		pos = [65, -75])
	blackcoin.draw()

	graycoin = visual.ImageStim(
		win = win,
		image = "assets/tutorial/coin.png",
		pos = [200, -200])
	graycoin.draw()
	
	spaceToContinue(win)
	win.flip()
	event.waitKeys()

def screen2(win):
	text = "This machine can make coins."
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 250],
		color = [-1, -1, -1],
		height = 40)
	textStim.draw()

	machine = visual.ImageStim(
		win = win,
		image = "assets/tutorial/machine.png",
		pos = [0, 0])
	machine.draw()
	spaceToContinue(win)
	win.flip()
	event.waitKeys()

	text2 = "You can control the machine using the U, I, O, and P keys."
	textStim2 = visual.TextStim(
		win = win,
		text = text2,
		pos = [0, -300],
		color = [-1, -1, -1],
		height = 30)
	textStim2.draw()
	machine.draw()
	textStim.draw()
	spaceToContinue(win)
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

	drawBlankTask(win, True)
	win.flip()
	keyPresses.append(getKeysTutorial())

	textStim.draw()
	drawBlankTask(win, True)
	showKeysTutorial(win, keyPresses)
	win.flip()
	keyPresses.append(getKeysTutorial())
	
	textStim.draw()
	drawBlankTask(win, True)
	showKeysTutorial(win, keyPresses)
	win.flip()
	keyPresses.append(getKeysTutorial())

	textStim.draw()
	drawBlankTask(win, True)
	showKeysTutorial(win, keyPresses)
	win.flip()
	keyPresses.append(getKeysTutorial())

	textStim.draw()
	drawBlankTask(win, True)
	showKeysTutorial(win, keyPresses)
	unlockCoin(win, "assets/smoke.png")
	spaceToContinue(win)
	win.flip()
	event.waitKeys()

def screen4(win):
	def screen4Text0(win):
		text = "You earn points by unlocking the coin in the box."
		textStim = visual.TextStim(
			win = win,
			text = text,
			pos = [-500, 0],
			color = [-1, -1, -1],
			height = 30,
			wrapWidth = 275)
		textStim.draw()

	def screen4Text1(win):
		"""Shows the text instructions for the first screen
		of the tutorial."""
		text = "To start, try pressing the I key."
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
		text = "Now try pressing O."
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
		text = "A hammer started shaping a coin. Seems like we're on the right track! \n \n Now try pressing U"
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
		text = "Now try pressing P."
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
		text = "A chisel started working after you pressed U and P! Then, a coin popped out of the machine. Congratulations!"
		textStim = visual.TextStim(
			win = win,
			text = text,
			pos = [-500, 0],
			color = [-1, -1, -1],
			height = 30,
			wrapWidth = 350)
		textStim.draw()
	
	text = "Unlocking coins can be hard! Luckily for you, this machine will show you the tools it's using as it makes the coins. This will help you figure out if you're on the right track."
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 0],
		color = [-1, -1, -1],
		height = 50)
	textStim.draw()
	spaceToContinue(win)
	win.flip()
	event.waitKeys()

	drawBlankTask(win, True)
	setGoalCoin(win)
	spaceToContinue(win)
	screen4Text0(win)
	win.flip()
	event.waitKeys()

	drawBlankTask(win, True)
	setGoalCoin(win)
	screen4Text1(win)
	win.flip()
	event.waitKeys(keyList = ["i"])

	drawBlankTask(win, True)
	setGoalCoin(win)
	showKeysTutorial(win, ["i"])
	screen4Text2(win)
	win.flip()
	event.waitKeys(keyList = ["o"])

	drawBlankTask(win, True)
	setGoalCoin(win)
	drawHammer(win)
	showKeysTutorial(win, ["i", "o"])
	screen4Text3(win)
	win.flip()
	event.waitKeys(keyList = ["u"])

	drawBlankTask(win, True)
	setGoalCoin(win)
	drawHammer(win)
	showKeysTutorial(win, ["i", "o", "u"])
	screen4Text4(win)
	win.flip()
	event.waitKeys(keyList = ["p"])

	drawBlankTask(win, True)
	highlightAndUnlock(win, "assets/tutorial/coin.png")
	unlockCoin(win, "assets/tutorial/coin.png")
	drawHammer(win)
	drawChisel(win)
	showKeysTutorial(win, ["i", "o", "u", "p"])
	screen4Text5(win)
	spaceToContinue(win)
	win.flip()
	event.waitKeys()

def screen5(win):
	text = "Great practice, now let’s move to the real game, with a new machine. This new machine makes stars, so you will learn to unlock stars instead of coins. This new machine also has different internal mechanisms, but they can still help you figure out how to unlock stars, as in the practice. Try your best!"
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 150],
		color = [-1, -1, -1],
		height = 40)
	textStim.draw()

	text2 = "Do you have any questions?"
	textStim2 = visual.TextStim(
		win = win,
		text = text2,
		pos = [0, -200],
		color = [-1, -1, -1],
		height = 40)
	textStim2.draw()

	spaceToContinue(win)
	win.flip()
	event.waitKeys()

def runTutorial(win):
	screen1(win)
	screen2(win)
	screen3(win)
	screen4(win)
	screen5(win)
