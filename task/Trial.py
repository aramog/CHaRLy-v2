from taskHelpers import *

from psychopy import event
import time

#TRIAL SWITCHES
POINTS_PER_STAR = 100
HOLD_SCREEN_TIME = .8 #how long to leave the last screen of a trial up
WAIT_TIME = .3 #inter trial interval

class Trial:
	def __init__(self, rules, star, block, label):
		#unpacks rules into instance vars
		self.lowRules = rules[0]
		self.highRules = rules[1]
		#specifiies star and block for runTrial
		self.star = star
		self.block = block
		self.keys = None
		self.rts = None
		self.unlock = -1
		self.label = label

	def runTrial(self):
		keyHist = [] #running cache of a trial's key presses
		reactionTimes = [] #stores reaction times
		#runs the sequence of updates to complete a 4 keystroke trial
		self.updateWindow(keyHist, reactionTimes)
		self.updateWindow(keyHist, reactionTimes)
		self.updateWindow(keyHist, reactionTimes)
		self.updateWindow(keyHist, reactionTimes)
		#last screen possibly unlocks highest layer item and finishes trial
		self.lastScreen(keyHist)
		self.keys = keyHist
		self.rts = reactionTimes

	def updateWindow(self, keyHist, reactionTimes):
		"""Gets input from user and makes the env. react according to
		the parameters of the trial."""
		drawBlankTask(self.block.win) #sets up the screen
		setGoalStar(self.block.win, self.star)
		pointCounter(self.block.win, self.block.points) #shows current points
		showKeys(self.block.win, keyHist) 
		self.checkLowSeq(keyHist) #checks and shows if a machine part has been unlocked
		self.block.win.flip() #display all changes to user
		start = time.time()
		keyHist.append(getKeys()) #get and record next key stroke.
		reactionTimes.append(time.time() - start)

	def lastScreen(self, keyHist):
		"""Runs the last window for a trial, unlocking a highest layer 
		item if the sequence was correct."""
		drawBlankTask(self.block.win)
		setGoalStar(self.block.win, self.star)
		showKeys(self.block.win, keyHist)
		self.checkLowSeq(keyHist)
		self.checkHighSeq(keyHist)
		pointCounter(self.block.win, self.block.points)
		self.block.win.flip()
		time.sleep(HOLD_SCREEN_TIME)
		blankScreen(self.block.win)
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
		i = 0 #counts number of items unlocked
		for combo in combos:
			for key, value in self.lowRules.items():
				match1 = combo[0] == value[0]
				match2 = combo[1] == value[1]
				if match1 and match2:
					self.showPart(key, i)
					i += 1

	def checkHighSeq(self, keyHist):
		"""Checks if a user unlocked a star. Awards points if correct star"""
		#gets the flat rules to compare to keyHist
		starRules = self.flatStarRules()
		print(starRules)
		print(keyHist)
		anyMatch = False
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
				anyMatch = True
				self.unlock = j + 1
				if j == 0:
					unlockStar(self.block.win, "./assets/black-star.png")
				elif j == 1:
					unlockStar(self.block.win, "./assets/orange-star.png")
				elif j == 2:
					unlockStar(self.block.win, "./assets/blue-star.png")
				elif j == 3:
					unlockStar(self.block.win, "./assets/gray-star.png")
				elif j == 4:
					unlockStar(self.block.win, "./assets/brown-star.png")
				elif j == 5:
					unlockStar(self.block.win, "./assets/cream-star.png")

				if j + 1 == self.star:
					self.block.points += POINTS_PER_STAR
					if j == 0:
						highlightAndUnlock(self.block.win, "./assets/black-star.png")
					elif j == 1:
						highlightAndUnlock(self.block.win, "./assets/orange-star.png")
					elif j == 2:
						highlightAndUnlock(self.block.win, "./assets/blue-star.png")
					elif j == 3:
						highlightAndUnlock(self.block.win, "./assets/gray-star.png")
					elif j == 4:
						highlightAndUnlock(self.block.win, "./assets/brown-star.png")
					elif j == 5:
						highlightAndUnlock(self.block.win, "./assets/cream-star.png")
				break

		if not anyMatch:
			unlockStar(self.block.win, "./assets/smoke.png")

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

	def showPart(self, partNumber, itemsOnScreen = 0):
		"""Given a part number, calls the correct 
		helper function to show the part."""
		if (not self.block.reactive):
			#if the block isn't reactive, don't want to show any parts
			return
		if partNumber == 1:
			drawGear(self.block.win, itemsOnScreen)
		elif partNumber == 2:
			drawLight(self.block.win, itemsOnScreen)
		elif partNumber == 3:
			drawPower(self.block.win, itemsOnScreen)
		elif partNumber == 4:
			drawFan(self.block.win, itemsOnScreen)

	def getData(self):
		"""Returns a dictionary of all the data related to the trial."""
		res = {
			"rules": [self.lowRules, self.highRules],
			"key_press": self.keys,
			"reaction_times": self.rts, 
			"star": self.star,
			"trial_type": self.label,
			"points": self.block.points,
			"unlock": self.unlock
		}
		return res
