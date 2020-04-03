import numpy as np
from itertools import product

class Agent:
	#base class for an agent, defines what methods should be implemented.
	#task params that should be fixed unless the task itself is redesigned
	NUM_ACTIONS = 4
	NUM_ITEMS = 4
	NUM_STARS = 4
	def __init__(self):
		self.action_space = list(range(self.NUM_ACTIONS)) #how many possible key presses there are
		self.state_space = self.make_state_space()

	def make_state_space(self):
		"""Using the fixed task params, will featurize all possible states.
		Taking the naive set product between all key, item, and star possibilities"""
		#all possible keys that could be on screen
		single_keys = set([(key) for key in self.action_space])
		double_keys = set(product(single_keys, repeat = 2))
		triple_keys = set(product(single_keys, repeat = 3))
		all_keys = {-1}.union(single_keys, double_keys, triple_keys) #{-1} is when no keys are on screen
		#all possible items that could be on screen
		single_items = set([(item) for item in range(self.NUM_ITEMS)])
		double_items = set(product(single_items, repeat = 2))
		all_items = {-1}.union(single_items, double_items)
		#all possible stars that could be a goal
		stars = set([(star) for star in range(self.NUM_STARS)])
		#returns the product set
		return set(product(all_keys, all_items, stars))

	def featurize(self, state):
		"""Returns the tuple style feature representation of the state."""
		#have all the special cases because of the way I did the state space
		if len(state.keys) > 1:
			keys = tuple(state.keys)
		elif len(state.keys) == 1:
			keys = state.keys[0]
		else:
			keys = (-1)
		if len(state.items) > 1:
			items = tuple(state.items)
		elif len(state.items) == 1:
			items = state.items[0]
		else:
			items = (-1)
		star = state.goalStar
		return (keys, items, star)

	def observe(self, state, reward):
		"""After taking an action, the environment will return a new state 
		and reward. This function integrates that information into the agent."""
		pass

	def policy(self):
		"""After an observation, the agent's policy will return the action 
		in current state. Note that the policy function assumes a state attribute."""
		pass

	def reset(self, inital_state):
		"""Given a starting state, the agent resets all its attributes."""
		self.curr_state = self.featurize(inital_state)

class RandomAgent(Agent):
	#simplest agent possible, just to test things out
	def policy(self):
		return np.random.choice(self.action_space)


		