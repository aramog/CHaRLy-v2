import numpy as np

class Agent:
	#base class for an agent, defines what methods should be implemented.
	def __init__(self, action_space = 4):
		self.action_space = list(range(4)) #how many possible key presses there are

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
		self.curr_state = inital_state
		self.reset_values()

	def reset_values(self):
		"""Depending on the value representations of the agent in question,
		this function will reset them to start a fresh agent."""
		pass

class RandomAgent(Agent):
	#simplest agent possible, just to test things out
	def policy(self):
		return np.random.choice(self.action_space)