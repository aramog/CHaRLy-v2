from utils import keyHandler, showStarSwitchScreen
import time

class Trial:
	"""Generic trial object. Stores all rules and is workhouse
	for task logic in checking for correct unlock sequences."""
	def __init__(self, rules, goal, machine):
		self.lowRules = rules[0]
		self.highRules = rules[1]
		self.goal = goal
		self.machine = machine
		#sets up variables that will be used throughout execution of a trial
		self.keys = []
		self.items = []
		self.reactionTimes = []
		self.unlock = -1

	def runTrial(self):
		"""Runs a sequence of 4 keys and checks whether a goal or any middle layer
		items were unlocked, calls visualization module to print things to the screen."""
		#first have to update the goal of the machine, so that visualization is consistent
		self.machine.updateGoal(self.goal)
		self.machine.blankTask()
		for i in range(4):
			#a trial is a run of 4 key presses
			keyPress, rt = keyHandler(self.machine.keyMap)
			self.keys.append(keyPress)
			#shows the key press on the screen
			self.reactionTimes.append(rt)
			unlockedItem = self.checkLowSeq()
			if unlockedItem >= 0:
				#means we unlocked something
				self.items.append(unlockedItem)
			#visualizes the current state
			if i < 3:
				#don't do the last state, that is handled below
				self.machine.updateWindow(self.keys, self.items, -1)
		#now that all keys have been pressed checks if a goal has been unlocked
		self.unlock = self.checkHighSeq(self.items)
		self.machine.updateWindow(self.keys, self.items, self.unlock, True) #prints the goal to the screen
		self.machine.resetWindow() #cleans up the canvas for the next trial
		return self.unlock, self.goal, self.getData() #passes the data from this trial back to the block

	def checkLowSeq(self):
		"""Based on what's currently in self.keys, returns the index of the middle layer item
		unlocked from the key presses. Some edge cases:
		- Returns -1 if no item is unlocked
		- Doesn't check for odd number runs (specifically chunk unlocks to 2nd and 4th key presses)
		- Only returns the unlock for the 3rd and the 4th keys in len(keys) == 4"""
		if len(self.keys) % 2:
			#can't unlock things on odd numbered keys
			return -1
		potentialSeq = (self.keys[-2], self.keys[-1]) #picks the last 2 keys pressed
		for item, rule in self.lowRules.items():
			#iterates over all the low level rules to see if something is unlocked
			if self.checkSeq(rule, potentialSeq):
				#means we have a valid sequence for this item
				return item
		return -1 #means nothing was unlocked

	def checkHighSeq(self, itemSeq):
		"""Given a sequence of unlocked items, checks if that forms a valid goal sequence."""
		if len(itemSeq) < 2: 
			#means we didn't unlock 2 middle layer items, so impossible to unlock a goal
			return -1
		for goal, rule in self.highRules.items():
			if self.checkSeq(rule, itemSeq):
				return goal
		return -1 #means we didn't unlock anything

	def checkSeq(self, rule, seq):
		"""Given a rule and a sequence, returns True only if they match."""
		return rule[0] == seq[0] and rule[1] == seq[1]

	def getData(self):
		"""Returns a dictionary containing all the relevant information for this trial."""
		res = {
			"rules": [self.lowRules, self.highRules],
			"key_press": self.keys,
			"reaction_times": self.reactionTimes, 
			"star": self.goal,
			"unlock": self.unlock
		}
		return res

class SwitchStarScreen:
	"""Like a trial, except it's run trial method only indicates that the goal star is changing."""
	HOLD_TIME = 2
	def __init__(self, machine, star):
		self.machine = machine
		self.star = star
	
	def runTrial(self):
		showStarSwitchScreen(self.machine.window, self.machine.assets["goal%s"%self.star])
		time.sleep(self.HOLD_TIME)
		return [-1, -2, dict()]

	def __repr__(self):
		return "break trial"





