class GameState:
	"""Class that represents the game state of charly. Designed such that all the information
	available to human participants is in the data structure."""
	def __init__(self, keys = [], items = [], goalStar = 0, unlockedStar = -1):
		"""Sets up all the starting params. If none are provided, a blank game
		is initialized."""
		self.keys = keys #which keys have been pressed. elts in range(4).
		self.items = items #which middle layer items are on the screen
		self.goalStar = goalStar #which star is highlighted in the box
		self.unlockedStar = unlockedStar #which star has been unlocked

	def copy(self):
		"""Returns a copy of the current game state."""
		return GameState(self.keys.copy(), self.items.copy(), self.goalStar, self.unlockedStar)