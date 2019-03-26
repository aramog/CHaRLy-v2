from taskHelpers import *
from Trial import *

from psychopy import visual

#BLOCK SWITCHES
LEARNING_TRIALS = 5
TRANSFER_TRIALS = 5

class Block:
	"""Generic block class. Initializes all rules and trials for
	learning and transfer phase."""
	def __init__(self, reactive, win):
		self.learningRules, self.transferRules = self.getRules()
		self.reactive = reactive
		self.points = 0
		self.win = win #pyschopy window for drawing
		
		self.learningTrials = []
		#create learning trials
		for i in range(LEARNING_TRIALS):
			#way to alternate highlighted star every 25 trials
			if (i % 50 < 25):
				star = 1
			else:
				star = 2
			self.learningTrials.append(Trial(self.learningRules, star, self))

		self.transferTrials = []
		#create transfer trials
		for i in range(TRANSFER_TRIALS):
			#way to alternate highlighted star every 25 trials
			if (i % 50 < 25):
				star = 1
			else:
				star = 2
			self.transferTrials.append(Trial(self.transferRules, star, self))

	def runBlock(self):
		for trial in self.learningTrials:
			trial.runTrial()

		for trial in self.transferTrials:
			trial.runTrial()

class HighTransferBlock(Block):
	def getRules(self):
		#will eventually have some random rule selection procedure
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
