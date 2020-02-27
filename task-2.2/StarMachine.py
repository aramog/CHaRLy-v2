from psychopy import visual
import time

from Machine import Machine
from Block import Block


class StarMachine(Machine):
	"""Implementation of the abstract machine class for the star machine."""
	assets = {
		"machine": "./assets/starMachine.jpg",
		"goal-1": "./assets/goal-1.png",
		"goal0": "./assets/goal0.png",
		"goal1": "./assets/goal1.png",
		"goal2": "./assets/goal2.png",
		"item0": "./assets/item0.png",
		"item1": "./assets/item1.png",
		"item2": "./assets/item2.png",
		"key0": "./assets/key0.png",
		"key1": "./assets/key1.png",
		"key2": "./assets/key2.png",
		"key3": "./assets/key3.png"
	}
	holdTime = .3
	waitTime = .3
	rules = [
		{0: (1, 0), 1: (3, 1), 2: (0, 2)},
		{0: (0, 1), 1: (1, 2), 2: (2, 0)}
	]
	goalSequence = [0, 1, 0, 1, 0, 1, 0, 1, 2, 2]
	keyMap = {"d": 0, "f": 1, "j": 2, "k": 3}
	#inverseKeyMap = {0: "d", 1: "f", 2: "j", 3: "k"}
	def __init__(self, window, reactive = True):
		"""Pretty much just for setting up basic params."""
		self.window = window
		self.goal = self.goalSequence[0]
		#sets up the block for the machine
		self.block = Block(self)
		self.reactive = reactive
		self.points = 0

	def showKeys(self, keys):
		"""Show a low level key press on the screen."""
		for i in range(len(keys)):
			#put keys[i] on the screen in the correct position
			keyText = visual.ImageStim(
				win = self.window,
				image = self.assets["key" + str(keys[i])],
				pos = [-95 + i*60, -250])
			keyText.size = [keyText.size[0] * .25, keyText.size[1] * .25]
			keyText.draw()

	def showItems(self, items):
		"""Item is one of the middle layer items that could be unlocked. Will display the item
		on the current canvas."""
		for i in range(len(items)):
			itemStim = visual.ImageStim(
				win = self.window,
				image = self.assets["item" + str(items[i])],
				pos = [-60 + i*60, -40])
			itemStim.draw()

	def showGoal(self, unlockedGoal):
		"""Same idea as the showItem method, but now for the higher level goal objects.
		unlockedGoal = -1 is a flag to show the null result at the end of a trial."""
		star = visual.ImageStim(
			win = self.window,
			image = self.assets["goal" + str(unlockedGoal)],
			pos = [-100, -150])
		star.draw()

	def showPoints(self):
		"""Draws a point counter for the given number of 
		points."""
		scoreText = visual.TextStim(
			win = self.window,
			text = "Points: " + str(self.points),
			pos = [0, 200],
			color = [-1, -1, -1],
			bold = True)
		scoreText.draw()
	
	def drawGoal(self):
		"""Draws the goal box and star on the screen."""
		assetString = "goal" + str(self.goal) #so we can index into assets and get the picture
		#draws the star
		star = visual.ImageStim(
			win = self.window,
			image = self.assets[assetString],
			pos = [0, 300])
		star.draw()
		#draws the box around it
		highlightBox = visual.Rect(
			win = self.window,
			width = 110,
			height = 110,
			pos = [0, 300],
			lineColor = [-1, -1, -1],
			lineWidth = 5)
		highlightBox.draw()

	def updateWindow(self, keys, items, goal, lastTrial = False):
		"""The current set of keys that have been pressed, items that they've unlocked, and goal
		that has been unlocked fully defines the state of the machine at any given trial. As such,
		with these three parameters, this method will display the current state of the machine on screen."""
		#first draws a new window
		self.setupScreen()
		#puts all the keys on it
		self.showKeys(keys)
		#put all the items on it only if the machine is reactive
		if self.reactive:
			self.showItems(items)		
		#if we unlocked a star, put it on the screen
		if goal >= 0:
			self.showGoal(goal)
		#means we haven't unlocked a star, but need to show some feedback, so we show the cloud.
		if lastTrial and goal < 0:
			self.showGoal(-1)
		#prints the updates on the window
		self.window.flip()

	def resetWindow(self):
		"""Using the params given for the hold and break times on the screen, wipes the window."""
		time.sleep(self.holdTime)
		self.window.flip()
		time.sleep(self.waitTime)

	def setupScreen(self):
		"""Draws the template for the rest of the task. Huge helper function for pretty much everything else."""
		#draws the machine itself
		machine = visual.ImageStim(
			win = self.window,
			image = self.assets["machine"]
		)
		machine.draw()
		#blocks out the window in the star machine
		windowCover = visual.Rect(
			win = self.window,
			fillColor = [1, 1, 1],
			pos = [-35, -40],
			width = 135,
			height = 65
		)
		windowCover.draw()
		#draws the bow that will show the keys
		key_hist = visual.Rect(
			win = self.window,
			width = 250,
			height = 75,
			pos = [0, -250],
			lineColor = [-1, -1, -1],
			lineWidth = 5)
		key_hist.draw()

		key_divide = visual.Line(
			win = self.window,
			start = [0, -287.5],
			end = [0, -212.5],
			lineColor = [-1, -1, -1],
			lineWidth = 5)
		key_divide.draw()
		if self.goal >= 0:
			#means we have a valid goal, so we should show it on the screen
			self.drawGoal()
		self.showPoints()

	def blankTask(self):
		"""Called after resetWindow and updatePoints. Will show a new blank task screen that can start
		a trial."""
		self.setupScreen()
		self.window.flip()

	def updatePoints(self, points):
		"""Updates how many points the user currently has to print on screen."""
		self.points = points

	def updateGoal(self, goal):
		"""Updates the current goal for visualization reasons."""
		self.goal = goal



