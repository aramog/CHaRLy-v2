from psychopy import visual
import time
import numpy as np

from Machine import Machine
from Block import Block


class StarMachine(Machine):
	"""Implementation of the abstract machine class for the star machine."""
	holdTime = .6
	waitTime = .3
	#TODO: Maybe randomize these orders
	learningSequence = [0, 1, 2, 3] * 3
	base = [1, 2]
	np.random.shuffle(base)
	transferSequence = base * 3
	def __init__(self, window, reactive = True, lenGoalSeq = 25):
		"""Pretty much just for setting up basic params."""
		self.window = window
		self.goal = self.learningSequence[0]
		self.rules = self.getRules()
		self.learningRules = self.rules[0]
		self.transferRules = self.rules[1]
		#randomizes the high level rules, might not need to do this if we change middle images
		self.learningRules[1], self.transferRules[1] = self.permuteRules(self.learningRules[1], self.transferRules[1])
		#sets up the block for the machine
		self.block = Block(self, lenGoalSeq)
		self.reactive = reactive
		self.points = 0

	def setKeyMap(self):
		self.keyMap = self.randomKeyMap()

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

	def randomKeyMap(self):
		"""Returns a mapping between the d, f, j, k keys and the 
		numerical indicies used in rules. Randomized."""
		keys = self.keys #can change to change the input keys to the machine
		nums = list(range(4))
		np.random.shuffle(nums) #where we randomize
		keyMap = dict()
		for i in range(4):
			keyMap[keys[i]] = nums[i]
		return keyMap

	def getRules(self):
		"""Method implemented by the low and high transfer machines."""
		pass

	def permuteRules(self, learningRules, transferRules):
		"""Given a ruleDict mapping numbers to tuples, permutes the keys of the dictionary."""
		#TODO: Try with and with out permuting to get a feel for which is easier.
		return learningRules, transferRules
		keys = list(learningRules.keys())
		learningValues = list(learningRules.values())
		transferValues = list(transferRules.values())
		np.random.shuffle(keys)
		learningPerm = dict()
		transferPerm = dict()
		for i in range(len(keys)):
			learningPerm[keys[i]] = learningValues[i]
			transferPerm[keys[i]] = transferValues[i]
		return learningPerm, transferPerm

class highTransferStarMachine(StarMachine):
	assets = {
		"machine": "./assets/starMachineA.jpg",
		"goal-1": "./assets/goal-1.png",
		"goal0": "./assets/goal0A.png",
		"goal1": "./assets/goal1A.png",
		"goal2": "./assets/goal2A.png",
		"goal3": "./assets/goal3A.png",
		"item0": "./assets/item0A.png",
		"item1": "./assets/item1A.png",
		"item2": "./assets/item2A.png",
		"item3": "./assets/item3A.png",
		"key0": "./assets/key0.png",
		"key1": "./assets/key1.png",
		"key2": "./assets/key2.png",
		"key3": "./assets/key3.png"
	}
	MACHINE_TYPE = "high"
	def getRules(self):
		middleRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		learningRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		transferRules = {0: (0, 1), 1: (2, 1), 2: (3, 2), 3: (3, 0)}
		return [middleRules, learningRules], [middleRules, transferRules]

class lowTransferStarMachine(StarMachine):
	assets = {
		"machine": "./assets/starMachineB.jpg",
		"goal-1": "./assets/goal-1.png",
		"goal0": "./assets/goal0B.png",
		"goal1": "./assets/goal1B.png",
		"goal2": "./assets/goal2B.png",
		"goal3": "./assets/goal3B.png",
		"item0": "./assets/item0B.png",
		"item1": "./assets/item1B.png",
		"item2": "./assets/item2B.png",
		"item3": "./assets/item3B.png",
		"key0": "./assets/key0.png",
		"key1": "./assets/key1.png",
		"key2": "./assets/key2.png",
		"key3": "./assets/key3.png"
	}
	MACHINE_TYPE = "low"
	def getRules(self):
		highRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		learningRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		transferRules = {0: (0, 1), 1: (2, 3), 2: (0, 2), 3: (3, 1)}
		return [learningRules, highRules], [transferRules, highRules]




