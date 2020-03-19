class Machine:
	"""This is the base class for a machines in the task that handle all the visualization and user
	interface for the task. Usage is that it is queried by the task logic modules in order to 
	print the result of key presses to the screen. Has the following attributes:
	- Key map: mapping between the keys pressed and the numbers in the rule sets.
	- Hold time: how long to leave the current frame on screen before wiping (for resetWindow).
	- Break time: how long to show a blank screen before showing the next trial.
	- Window: psychopy environment for showing things on the screen"""
	def updateWindow(self):
		"""The current set of keys that have been pressed, items that they've unlocked, and goal
		that has been unlocked fully defines the state of the machine at any given trial. As such,
		with these three parameters, this method will display the current state of the machine on screen."""
		pass

	def resetWindow(self):
		"""Using the params given for the hold and break times on the screen, wipes the window."""
		pass

	def blankTask(self):
		"""Called after resetWindow and updatePoints. Will show a new blank task screen that can start
		a trial."""
		pass

	def updatePoints(self, points):
		"""Updates how many points the user currently has to print on screen."""
		pass

	def updateGoal(self, goal):
		"""Updates the current goal for visualization reasons."""
		pass
