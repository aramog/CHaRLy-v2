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

			self.keyPress(keyHist)
			self.keyPress(keyHist)
			self.keyPress(keyHist)
			self.keyPress(keyHist)

			# TODO: add functionality for the last screen in a trial

		def keyPress(self, keyHist):
			"""Runs a single key press for one trial"""
			drawBlankTask(self.block.win)
			if (self.star == 1):
				highlightBlackStar(self.block.win)
			else:
				highlightOrangeStar(self.block.win)
			pointCounter(self.block.win, self.block.points)
			showKeys(self.block.win, keyHist)
			checkLowSeq(keyHist)
			win.flip()
			keyHist.append(getKeys())

		def checkLowSeq(self, keyHist):
			"""Checks if the user unlocked a machine part."""
			if (len(keyHist) < 2):
				return

			elif (len(keyHist) < 4):
				combos = [(keyHist[len(keyHist) - 2], keyHist[len(keyHist) - 1])]

			elif (len(keyHist) == 4):
				combos = [(keyHist[0], keyHist[1]), (keyHist[2], keyHist[3])]

			#check what parts have been unlocked
			for combo in combos:
				for key, value in self.lowRules.items():
					match1 = combo[0] == value[0]
					match2 = combo[1] == value[1]
					if match1 and match2:
						self.showPart(key)

		def showPart(self, partNumber):
			"""Given a part number, calls the correct 
			helper function to show the part."""
			if partNumber == 1:
				drawGear(self.block.win)
			elif partNumber == 2:
				drawLight(self.block.win)
			else:
				# TODO: add the other part visuals
				return


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
				star = 2
			self.learningTrials.append(Trial(self.learningRules), star, self)

		self.transferTrials = []
		#create transfer trials
		for i in range(250):
			#way to alternate highlighted star every 25 trials
			if ((i % 25) % 2 == 0):
				star = 1
			else:
				star = 2
			self.transferTrials.append(Trial(self.transferRules), star, self)

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
