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

from tutorialHelpers import *
from StarMachine import StarMachine
from Block import Block
#TODO: Update this machine with new visual plotters
class CoinMachine(StarMachine):
	NUM_FREE_PLAY_TRIALS = 3
	assets = {
		"machine": "./assets/tutorial/machine.png",
		"goal-1": "./assets/goal-1.png",
		"goal0": "./assets/tutorial/coin.png",
		"item0": "./assets/tutorial/hammer.png",
		"item1": "./assets/tutorial/chisel.png",
		"key0": "./assets/tutorial/d.png",
		"key1": "./assets/tutorial/f.png",
		"key2": "./assets/tutorial/j.png",
		"key3": "./assets/tutorial/k.png"
	}
	MACHINE_TYPE = "tutorial"
	def getRules(self):
		highRules = {0: (0, 1)}
		lowRules = {0: (1, 2), 1: (0, 3)}
		return [lowRules, highRules], [lowRules, highRules]
	keyMap = {"d": 0, "f": 1, "j": 2, "k": 3}
	learningSequence = [0]
	transferSequence = []
	def __init__(self, window):
		self.window = window
		self.goal = 0
		self.rules = self.getRules()
		self.learningRules = self.rules[0]
		self.transferRules = self.rules[1]
		self.block = Block(self, self.NUM_FREE_PLAY_TRIALS)
		self.reactive = True
		self.points = 0

def screen1(win):
	text = "Your goal in this task is to collect coins."
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

	text2 = "You can control the machine using the D, F, J, and K keys."
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
	keyPresses.append(getKeys())

	textStim.draw()
	drawBlankTask(win, True)
	showKeysTutorial(win, keyPresses)
	win.flip()
	keyPresses.append(getKeys())
	
	textStim.draw()
	drawBlankTask(win, True)
	showKeysTutorial(win, keyPresses)
	win.flip()
	keyPresses.append(getKeys())

	textStim.draw()
	drawBlankTask(win, True)
	showKeysTutorial(win, keyPresses)
	win.flip()
	keyPresses.append(getKeys())

	textStim.draw()
	drawBlankTask(win, True)
	showKeysTutorial(win, keyPresses)
	unlockCoin(win, "assets/goal-1.png")
	spaceToContinue(win)
	win.flip()
	event.waitKeys()

def screen4(win):
	def screen4Text0(win):
		text = "Your goal is to make the coin in the black box above the machine."
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
		text = "To start, try pressing the F key."
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
		text = "Now try pressing J."
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
		text = "A hammer started shaping a coin. Seems like we're on the right track! \n \n Now try pressing D"
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
		text = "Now try pressing K."
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
		text = "A chisel started working after you pressed D and K! Then, a coin popped out of the machine. Congratulations!"
		textStim = visual.TextStim(
			win = win,
			text = text,
			pos = [-500, 0],
			color = [-1, -1, -1],
			height = 30,
			wrapWidth = 350)
		textStim.draw()
	
	text = "Collecting coins can be hard! Luckily, the machine uses tools when it makes coins. Seeing these tools can help you get on the right track."
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
	event.waitKeys(keyList = ["f"])

	drawBlankTask(win, True)
	setGoalCoin(win)
	showKeysTutorial(win, ["f"])
	screen4Text2(win)
	win.flip()
	event.waitKeys(keyList = ["j"])

	drawBlankTask(win, True)
	setGoalCoin(win)
	drawHammer(win)
	showKeysTutorial(win, ["f", "j"])
	screen4Text3(win)
	win.flip()
	event.waitKeys(keyList = ["d"])

	drawBlankTask(win, True)
	setGoalCoin(win)
	drawHammer(win)
	showKeysTutorial(win, ["f", "j", "d"])
	screen4Text4(win)
	win.flip()
	event.waitKeys(keyList = ["k"])

	drawBlankTask(win, True)
	highlightAndUnlock(win, "assets/tutorial/coin.png")
	unlockCoin(win, "assets/tutorial/coin.png")
	drawHammer(win)
	drawChisel(win)
	showKeysTutorial(win, ["f", "j", "d", "k"])
	screen4Text5(win)
	spaceToContinue(win)
	win.flip()
	event.waitKeys()

def screen5(win):
	"""Screen to show before free play with machine."""
	text = "Now that we've shown you how the machine works, you can try it out for yourself!"
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 0], 
		color = [-1, -1, -1],
		bold = True,
		height = 30)
	textStim.draw()
	spaceToContinue(win)
	win.flip()
	event.waitKeys()

def screen6(win):
	text = "Great job! Now let's move to a new machine, which makes stars instead of coins. This new machine uses different tools, but seeing them can still help you figure out how ot make stars. Try your best!"
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
	cm = CoinMachine(win)
	cm.block.runBlock()
	screen6(win)
