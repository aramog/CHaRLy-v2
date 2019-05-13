from taskHelpers import *
from Trial import *

from psychopy import visual

class Block:
	"""Generic block class. Initializes all rules and trials for
	learning and transfer phase."""
	def __init__(self, reactive, win, lenStarTrials):
		self.learningRules, self.negTransferRules, self.posTransferRules = self.getRules()
		self.reactive = reactive
		self.points = 0
		self.win = win #pyschopy window for drawing
		self.lenStarTrials = lenStarTrials
		#stores data for each trial.
		self.data = []
		
		self.learningTrials = []
		learningStarSeq = [2, 3, 2, 3, 1, 4, 1, 4, 
			1, 2, 1, 2, 3, 4, 3, 4]
		learningStarSeq.extend(self.randomOrder())
		self.makeTrials(
			self.learningTrials, learningStarSeq, self.learningRules, "learning")

		self.posTransferTrials = []
		posTransStarSeq = [5, 6, 5, 6]
		self.makeTrials(
			self.posTransferTrials, posTransStarSeq, self.posTransferRules, "pos_transfer")

		self.learning2Trials = []
		learning2StarSeq = self.randomOrder()
		self.makeTrials(
			self.learning2Trials, learning2StarSeq, self.learningRules, "learning2")

		self.negTransferTrials = []
		negTransStarSeq = self.randomOrder()
		self.makeTrials(
			self.negTransferTrials, negTransStarSeq, self.negTransferRules, "neg_trans")

	def makeTrials(self, trialList, starSeq, rules, trialLabel):
		"""Appends trial objects to trialList according to starSeq and rules."""
		for star in starSeq:
			for j in range(self.lenStarTrials):
				trialList.append(Trial(rules, star, self, trialLabel))

	def runBlock(self):
		#runs each sub block
		self.runSubBlock(self.learningTrials)
		breakScreen(self.win)
		self.runSubBlock(self.posTransferTrials)
		breakScreen(self.win)
		self.runSubBlock(self.learning2Trials)
		breakScreen(self.win)
		self.runSubBlock(self.negTransferTrials)

	def runSubBlock(self, trialList):
		"""Runs all the trials in trialList."""
		i, j = 0, 0
		while (i < len(trialList)):
			while (j < self.lenStarTrials):
				trialList[i].runTrial()
				self.data.append(trialList[i].getData())
				i, j = i + 1, j + 1
			breakScreen(self.win)
			j = 0

	def getData(self):
		"""Returns all data related to the block."""
		return self.data

	def randomOrder(self):
		"""Returns a random star order for part of the
		learning phase."""
		return [2, 1, 3, 4, 3, 2, 4, 1]

class HighTransferBlock(Block):
	def getRules(self):
		"""Rules are represented by a dictionary whose keys are the item number
		, and values the correct action sequence of lower level items needed to
		unlock it.
		rules[0] are rules for middle layer, rules[1] for top layer."""
		learningRules = [{1: (2, 4), 2: (2, 3), 3: (3, 1), 4: (4, 1)},
		{1: (1, 2), 2: (2, 3), 3: (4, 1), 4: (3, 4)}]
		negTransferRules = [{1: (2, 4), 2: (2, 3), 3: (3, 1), 4: (4, 1)},
		{1: (1, 2), 2: (2, 4), 3: (3, 1), 4: (3, 4)}]
		#TODO: Might need to update these rules
		posTransferRules = [{1: (2, 4), 2: (2, 3), 3: (3, 1), 4: (4, 1)},
		{5: (2, 3), 6: (4, 1)}]
		return learningRules, negTransferRules, posTransferRules

class LowTransferBlock(Block):
	def getRules(self):
		learningRules = [{1: (1, 2), 2: (2, 4), 3: (1, 3), 4: (3, 4)},
		 {1: (1, 4), 2: (2, 3)}]
		transferRules = [{1: (1, 4), 2: (3, 4), 3: (1, 2), 4: (3, 2)}, 
		{1: (1, 4), 2: (2, 3)}]
		return learningRules, transferRules
