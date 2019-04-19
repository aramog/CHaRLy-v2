from taskHelpers import *
from Trial import *

from psychopy import visual

class Block:
	"""Generic block class. Initializes all rules and trials for
	learning and transfer phase."""
	def __init__(self, reactive, win, 
		learningTrials, transferTrials, lenStarTrials):
		self.learningRules, self.transferRules = self.getRules()
		self.reactive = reactive
		self.points = 0
		self.win = win #pyschopy window for drawing
		self.numLearningTrials = learningTrials
		self.numTransferTrials = transferTrials
		self.lenStarTrials = lenStarTrials
		#stores data for each trial.
		self.learningData = []
		self.transferData = []
		
		self.learningTrials = []
		#create learning trials
		i, j, star = 0, 0, 1
		while (i < self.numLearningTrials):
			while (j < self.lenStarTrials):
				self.learningTrials.append(Trial(self.learningRules, star, self))
				j += 1
				i += 1
			star = star % 4 + 1
			j = 0

		self.transferTrials = []
		#create transfer trials
		i, j, star = 0, 0, 1
		while (i < self.numTransferTrials):
			while (j < self.lenStarTrials):
				self.transferTrials.append(Trial(self.transferRules, star, self))
				j += 1
				i += 1
			star = star % 4 + 1
			j = 0

	def runBlock(self):
		#loops through all the trials and records data
		for trial in self.learningTrials:
			trial.runTrial()
			self.learningData.append(trial.getData())

		breakScreen(win)

		for trial in self.transferTrials:
			trial.runTrial()
			self.transferData.append(trial.getData())

	def getData(self):
		"""Returns all data related to the block."""
		return self.learningData, self.transferData

class HighTransferBlock(Block):
	def getRules(self):
		"""Rules are represented by a dictionary whose keys are the item number
		, and values the correct action sequence of lower level items needed to
		unlock it.
		rules[0] are rules for middle layer, rules[1] for top layer."""
		learningRules = [{1: (2, 3), 2: (4, 1), 3: (3, 1), 4: (2, 4)}, 
		{1: (1, 3), 2: (4, 2), 3: (2, 3), 4: (4, 1)}]
		transferRules = [{1: (2, 3), 2: (4, 1), 3: (3, 1), 4: (2, 4)}, 
		{1: (1, 4), 2: (3, 2), 3: (2, 3), 4: (4, 1)}]
		return learningRules, transferRules

class LowTransferBlock(Block):
	def getRules(self):
		learningRules = [{1: (1, 2), 2: (2, 4), 3: (1, 3), 4: (3, 4)},
		 {1: (1, 4), 2: (2, 3)}]
		transferRules = [{1: (1, 4), 2: (3, 4), 3: (1, 2), 4: (3, 2)}, 
		{1: (1, 4), 2: (2, 3)}]
		return learningRules, transferRules
