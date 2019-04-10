from taskHelpers import *
from Trial import *

from psychopy import visual

#BLOCK SWITCHES
LEARNING_TRIALS = 6
TRANSFER_TRIALS = 0
LEN_STAR_TRIALS = 3 #how long to prioritize one star

class Block:
	"""Generic block class. Initializes all rules and trials for
	learning and transfer phase."""
	def __init__(self, reactive, win):
		self.learningRules, self.transferRules = self.getRules()
		self.reactive = reactive
		self.points = 0
		self.win = win #pyschopy window for drawing
		#stores data for each trial.
		self.learningData = []
		self.transferData = []
		
		self.learningTrials = []
		#create learning trials
		for i in range(LEARNING_TRIALS):
			#way to alternate highlighted star every LEN_STAR_TRIALS
			if (i % (LEN_STAR_TRIALS * 2) < LEN_STAR_TRIALS):
				star = 1
			else:
				star = 2
			#adds a trial object to sequence of learning trials
			self.learningTrials.append(Trial(self.learningRules, star, self))

		self.transferTrials = []
		#create transfer trials
		for i in range(TRANSFER_TRIALS):
			#way to alternate highlighted star every LEN_STAR_TRIALS
			if (i % (LEN_STAR_TRIALS * 2) < LEN_STAR_TRIALS):
				star = 1
			else:
				star = 2
			#adds a trial object to sequence of transfer trials
			self.transferTrials.append(Trial(self.transferRules, star, self))

	def runBlock(self):
		#loops through all the trials and records data
		for trial in self.learningTrials:
			trial.runTrial()
			self.learningData.append(trial.getData())

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
		{1: (1, 3), 2: (4, 2)}]
		transferRules = [{1: (2, 3), 2: (4, 1), 3: (3, 1), 4: (2, 4)}, 
		{1: (1, 4), 2: (3, 2)}]
		return learningRules, transferRules

class LowTransferBlock(Block):
	def getRules(self):
		learningRules = [{1: (1, 2), 2: (2, 4), 3: (1, 3), 4: (3, 4)},
		 {1: (1, 4), 2: (2, 3)}]
		transferRules = [{1: (1, 4), 2: (3, 4), 3: (1, 2), 4: (3, 2)}, 
		{1: (1, 4), 2: (2, 3)}]
		return learningRules, transferRules
