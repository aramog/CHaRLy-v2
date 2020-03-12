from Trial import Trial, SwitchStarScreen

POINT_PER_GOAL = 1
class Block:
	"""Generic block class. Highest level object in the task logic module.
	Contains the following:
	- Rules (both learning and transfer)
	- Trials (list of trial objects to execute)
	- Points (tally of current score within the block)"""
	def __init__(self, machine, lenGoalSeq = 25):
		"""Takes in the following parameters:
		- machine: defines the context for the task. Gives the rule set and the goal sequence.
		Also facilitates all the visualization at the trial level."""
		self.points = 0
		self.lenGoalSeq = lenGoalSeq
		self.machine = machine
		#constructs the list of trials to execute based on the goal seq
		self.learningTrials, self.transferTrials = self.makeTrials()

	def makeTrials(self):
		"""Returns a list of trial objects in the order they should be executed by the task."""
		#makes the learning trials
		learningTrials = []
		for goal in self.machine.learningSequence:
			breakScreen = SwitchStarScreen(self.machine, goal)
			learningTrials.append(breakScreen)
			for i in range(self.lenGoalSeq):
				#makes a new trial with this goal seq
				trial = Trial(self.machine.learningRules, goal, self.machine)
				learningTrials.append(trial)
			
		#makes the transfer trials
		transferTrials = []
		for goal in self.machine.transferSequence:
			breakScreen = SwitchStarScreen(self.machine, goal)
			transferTrials.append(breakScreen)
			for i in range(self.lenGoalSeq):
				#makes a new trial with this goal seq
				trial = Trial(self.machine.transferRules, goal, self.machine)
				transferTrials.append(trial)
		return learningTrials, transferTrials

	def runBlock(self):
		"""Runs all the trials in self.trials."""
		#manually sets up the first screen
		self.machine.blankTask()
		learningData = self.runSubBlock(self.learningTrials)
		transferData = self.runSubBlock(self.transferTrials)
		self.data = {"learning": learningData, "transfer": transferData}
		return self.data

	def runSubBlock(self, trialList):
		"""Given a list of trials, runs each trial and returns the data output."""
		self.machine.blankTask()
		data = []
		for trial in trialList:
			unlockedGoal, goal, trialData = trial.runTrial()
			#checks if we add points
			if unlockedGoal == goal:
				self.points += POINT_PER_GOAL
			#send updated points to the machine
			self.machine.updatePoints(self.points)
			if trialData: data.append(trialData)
			#draw a new blank task window for the next trial
			self.machine.blankTask()
		return data


	def getData(self):
		return self.data
