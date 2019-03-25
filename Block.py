from taskHelpers import *

from psychopy import visual

class Block:
	"""Generic block class. Initializes all rules and trials for
	learning and transfer phase."""
	class Trial:
		def __init__(self, rules, star, block):
			self.lowRules = rules[0]
			self.highRules = rules[1]
			self.star = star
			self.block = block

		def runTrial(self):
			keyHist = []
			
			#first key press
			drawBlankTask(self.block.win)
			if (self.star == 1):
				highlightBlackStar(self.block.win)
			else:
				highlightOrangeStar(self.block.win)
			pointCounter(self.block.win, self.block.points)
			keyHist.append(getKeys())
			showKeys(self.block.win, keyHist)
			win.flip()

			#second key press
			drawBlankTask(self.block.win)
			if (self.star == 1):
				highlightBlackStar(self.block.win)
			else:
				highlightOrangeStar(self.block.win)
			pointCounter(self.block.win, self.block.points)
			keyHist.append(getKeys())
			showKeys(self.block.win, keyHist)
			# TODO: check if key seq is correct
			win.flip()

			#third key press
			drawBlankTask(self.block.win)
			if (self.star == 1):
				highlightBlackStar(self.block.win)
			else:
				highlightOrangeStar(self.block.win)
			pointCounter(self.block.win, self.block.points)
			keyHist.append(getKeys())
			showKeys(self.block.win, keyHist)
			win.flip()

			#fourth key press
			drawBlankTask(self.block.win)
			if (self.star == 1):
				highlightBlackStar(self.block.win)
			else:
				highlightOrangeStar(self.block.win)
			pointCounter(self.block.win, self.block.points)
			keyHist.append(getKeys())
			showKeys(self.block.win, keyHist)
			win.flip()


	def __init__(self, reactive, win):
		self.learningRules, self.transferRules = self.getRules()
		self.reactive = reactive
		self.points = 0
		self.win = win #pyschopy window for drawing
		
		self.learningTrials = []
		#create learning trials
		for i in range(250):
			#way to alternate highlighted star every 25 trials
			if ((i % 25) % 2 == 0):
				star = 1
			else:
				star 0
			self.learningTrials.append(Trial(self.learningRules), star, self)

		self.transferTrials = []
		#create transfer trials
		for i in range(250):
			#way to alternate highlighted star every 25 trials
			if ((i % 25) % 2 == 0):
				star = 1
			else:
				star 0
			self.transferTrials.append(Trial(self.transferRules), star, self)

	def runBlock(self):
		for trial in self.learningTrials:
			trial.runTrial()

		for trial in self.transferTrials:
			trial.runTrial()

class HighTransferBlock(Block):
	def __init__(self, reactive):
		Block.__init__(self, reactive)

	def getRules(self):
		#will eventually have some random rule selection procedure
		learningRules = [[(2, 3), (4, 1), (3, 1), (2, 4)], [(1, 3), (4, 2)]]
		transferRules = [[(2, 3), (4, 1), (3, 1), (2, 4)], [(1, 4), (3, 2)]]
		return learningRules, transferRules

class LowTransferBlock(Block):
	def __init__(self, reactive):
		Block.__init__(self, reactive)

	def getRules(self):
		learningRules = [[(1, 2), (2, 4), (1, 3), (3, 4)], [(1, 4), (2, 3)]]
		transferRules = [[(1, 4), (3, 4), (1, 2), (3, 2)], [(1, 4), (2, 3)]]
		return learningRules, transferRules
