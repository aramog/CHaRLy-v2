from Trial import Trial

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
		self.rules = machine.rules
		self.points = 0
		self.goalSequence = machine.goalSequence
		self.lenGoalSeq = lenGoalSeq
		self.machine = machine
		#constructs the list of trials to execute based on the goal seq
		self.trials = self.makeTrials()

	def makeTrials(self):
		"""Returns a list of trial objects in the order they should be executed by the task."""
		trials = []
		for goal in self.goalSequence:
			for i in range(self.lenGoalSeq):
				#makes a new trial with this goal seq
				trial = Trial(self.rules, goal, self.machine)
				trials.append(trial)
		return trials

	def runBlock(self):
		"""Runs all the trials in self.trials."""
		#manually sets up the first screen
		self.machine.blankTask()
		data = []
		for trial in self.trials:
			unlockedGoal, goal, trialData = trial.runTrial()
			#checks if we add points
			if unlockedGoal == goal:
				self.points += POINT_PER_GOAL
			#send updated points to the machine
			self.machine.updatePoints(self.points)
			#draw a new blank task window for the next trial
			self.machine.blankTask()
			data.append(trialData)
		self.data = data
		return data

	def getData(self):
		return self.data