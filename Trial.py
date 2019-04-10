from taskHelpers import *

from psychopy import event
import time

#TRIAL SWITCHES
POINTS_PER_STAR = 100
WAIT_TIME = 1 #inter trial interval

class Trial:
	def __init__(self, rules, star, block):
		#unpacks rules into instance vars
		self.lowRules = rules[0]
		self.highRules = rules[1]
		#specifiies star and block for runTrial
		self.star = star
		self.block = block
		self.keys = None

	def runTrial(self):
		keyHist = [] #running cache of a trial's key presses
		#runs the sequence of updates to complete a 4 keystroke trial
		self.updateWindow(keyHist)
		self.updateWindow(keyHist)
		self.updateWindow(keyHist)
		self.updateWindow(keyHist)
		#last screen possibly unlocks highest layer item and finishes trial
		self.lastScreen(keyHist)
		self.keys = keyHist

	def updateWindow(self, keyHist):
		"""Gets input from user and makes the env. react according to
		the parameters of the trial."""
		drawBlankTask(self.block.win) #sets up the screen
		if (self.star == 1): #highlights correct star
			highlightBlackStar(self.block.win)
		else:
			highlightOrangeStar(self.block.win)
		pointCounter(self.block.win, self.block.points) #shows current points
		showKeys(self.block.win, keyHist) 
		self.checkLowSeq(keyHist) #checks and shows if a machine part has been unlocked
		self.block.win.flip() #display all changes to user
		keyHist.append(getKeys()) #get and record next key stroke.

	def lastScreen(self, keyHist):
		"""Runs the last window for a trial, unlocking a highest layer 
		item if the sequence was correct."""
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
		time.sleep(WAIT_TIME)

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
		#gets the flat rules to compare to keyHist
		starRules = self.flatStarRules()
		print(starRules)
		print(keyHist)
		for j in range(len(starRules)):
			match = True
			#iterates over the keys in a rule
			for i in range(len(keyHist)):
				if starRules[j][i] != keyHist[i]:
					#if key hist doesn't match rule, not a match
					match = False
					break
			if match:
				#means a star was unlocked
				if j == 0:
					unlockBlackStar(self.block.win)
				elif j == 1:
					unlockOrangeStar(self.block.win)
				#now check if we add points
				print(j)
				print(self.star)
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
				rule.extend([key for key in lowRule])
			rules.append(tuple(rule))
		return rules

	def showPart(self, partNumber):
		"""Given a part number, calls the correct 
		helper function to show the part."""
		if (not self.block.reactive):
			#if the block isn't reactive, don't want to show any parts
			return
		if partNumber == 1:
			drawGear(self.block.win)
		elif partNumber == 2:
			drawLight(self.block.win)
		elif partNumber == 3:
			drawPower(self.block.win)
		elif partNumber == 4:
			drawFan(self.block.win)

	def getData(self):
		"""Returns a dictionary of all the data related to the trial."""
		res = {
			"rules": [self.lowRules, self.highRules],
			"key_press": self.keys,
			"star": self.star,
			"trial_type": "learning_sequence",
			"points": self.block.points
		}
		return res
