from state import GameState
from task_logic import *

class Environment:
	"""Base class for the CHaRLy environment that defines the important methods."""
	def step(self, action):
		"""Given an action, returns the next state and reward."""
		pass

	def finished(self):
		"""Returns true if the task is over."""
		pass

	def reset(self):
		"""Resets all interal attributes and returns an initial state."""
		pass

class Charly(Environment):
	"""Class for the charly game."""
	def __init__(self, rules, transferIdx, starSequence, seqLength = 25):
		"""Sets up all the main params for the game."""
		self.learning_rules = rules[0]
		self.transfer_rules = rules[1]
		self.transferIdx = transferIdx * seqLength #the trial when we should use transfer rules instead of learning rules
		self.starSequence = self.get_full_sequence(starSequence, seqLength)
		self.curr_trial = 0

	def get_full_sequence(self, starSeq, seqLength):
		"""Returns a list where each element of starSeq is repeated seqLength times."""
		fullSeq = []
		for star in starSeq:
			fullSeq.extend([star for _ in range(seqLength)])
		return fullSeq

	def rules(self):
		"""Returns the current rule set, based on curr_trial."""
		#TODO: this might need to be a bit more nuanced, but I think it's fine.
		if self.curr_trial < self.transferIdx:
			return self.learning_rules
		else:
			return self.transfer_rules

	def step(self, action):
		"""Given an action, returns the next state and reward."""
		#TODO: Figure out how to show the agent the last package that appears when a star is unlocked
		#first integrates that action into the current game frame
		updated_state = update_game_state(self.state, self.rules(), action)
		#now computes the reward
		if updated_state.goalStar == updated_state.unlockedStar:
			reward = 1
		else:
			reward = 0
		self.state = updated_state
		return updated_state, reward

	def blank_state(self):
		"""Called after an episode of 4 key presses. Sets the interal state
		to a blank game state and increments the curr_trial counter."""
		self.curr_trial += 1
		new_state = GameState()
		new_state.goalStar = self.starSequence[self.curr_trial]
		self.state = new_state
		return self.state

	def finished(self):
		"""Returns true if the task is over."""
		return self.curr_trial >= len(self.starSequence) -1

	def reset(self):
		"""Resets all interal attributes and returns an initial state."""
		self.curr_trial = 0
		starting_state = GameState()
		starting_state.goalStar = self.starSequence[0] #set goal start to first in starSequence
		self.state = starting_state
		return starting_state


if __name__ == "__main__":
	env = Charly(*task_params())
	env.reset()
