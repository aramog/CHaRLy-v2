from taskHelpers import *

from psychopy import event

POINTS_PER_STAR = 100

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

		self.lastKeyPress(keyHist)

	def keyPress(self, keyHist):
		"""Runs a single key press for one trial"""
		drawBlankTask(self.block.win)
		if (self.star == 1):
			highlightBlackStar(self.block.win)
		else:
			highlightOrangeStar(self.block.win)
		pointCounter(self.block.win, self.block.points)
		showKeys(self.block.win, keyHist)
		self.checkLowSeq(keyHist)
		self.block.win.flip()
		keyHist.append(getKeys())

	def lastKeyPress(self, keyHist):
		"""Runs the last key press window for a trial."""
		drawBlankTask(self.block.win)
		if (self.star == 1):
			highlightBlackStar(self.block.win)
		else:
			highlightOrangeStar(self.block.win)
		showKeys(self.block.win, keyHist)
		self.checkLowSeq(keyHist)
		self.checkHighSeq(keyHist)
		pointCounter(self.block.win, self.block.points)
		self.block.win.flip()
		event.waitKeys()

	def checkLowSeq(self, keyHist):
		"""Checks if the user unlocked a machine part."""
		if (len(keyHist) < 2):
			return

		elif (len(keyHist) < 4):
			combos = [(keyHist[0], keyHist[1])]

		elif (len(keyHist) == 4):
			combos = [(keyHist[0], keyHist[1]), (keyHist[2], keyHist[3])]

		#check what parts have been unlocked
		for combo in combos:
			for key, value in self.lowRules.items():
				match1 = combo[0] == value[0]
				match2 = combo[1] == value[1]
				if match1 and match2:
					self.showPart(key)

	def checkHighSeq(self, keyHist):
		"""Checks if a user unlocked a star. Awards points if correct star"""
		# TODO: Some error in here from playing arounddf
		#gets the flat rules to compare to keyHist
		starRules = self.flatStarRules()
		for j in range(len(starRules)):
			match = True
			#iterates over the keys in a rule
			for i in range(len(keyHist)):
				if starRules[j][i] != keyHist[i]:
					#if key hist doesn't match rule, not a match
					match = False
			if match:
				#means a star was unlocked
				if j == 1:
					unlockBlackStar(self.block.win)
				elif j == 2:
					unlockOrangeStar(self.block.win)
				#now check if we add points
				if j + 1 == self.star:
					self.block.points += POINTS_PER_STAR
				break

	def flatStarRules(self):
		"""Returns a list of 2 4 action sequences associated with each star."""
		rules = []
		for key, value in self.highRules.items():
			rule = []
			#iterate the action seq and extract primitive sequence
			for part in value:
				lowRule = self.lowRules[part]
				rule.extend([key for key in self.lowRules])
			rules.append(tuple(rule))
		return rules

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
