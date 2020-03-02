"""
Several base clases to serve as the template for more complex agents.
"""

from util import *

class Agent:
	"""
	An agent is an object with a getAction(state) method.
	"""
	def __init__(self, index=0):
		self.index = index

	def getAction(self, state):
		"""
		Given a game state, the agent will return an action.
		"""
		raiseNotDefined()

class ValueEstimationAgent(Agent):
	"""
	Abstraction for any agent that computes action-value (q) estimates.

	V(s) = max_{a in actions} Q(s, a)
	policy(s) = argmax_{a in actions} Q(s, a)
	"""
	def __init__(self, alpha=1.0, epsilon=.05, gamma=.8):
		"""
		alpha - learning rate
		epsilon - exploration rate
		gamma - discount factor
		"""
		self.alpha = alpha
		self.epsilon = epsilon
		self.discount = gamma

	def getQValue(self, state, action):
		"""
		Returns Q(state, action)
		"""
		raiseNotDefined()

	def getValue(self, state):
		"""
		Returns max_{a in actions} Q(s, a)
		"""
		raiseNotDefined()

	def getPolicy(self, state):
		"""
		Returns argmax_{a in actions} Q(s, a)
		"""
		raiseNotDefined()

	def getAction(self, state):
		"""
		Takes a greedy action with prob 1 - epsilon. Otherwise
		will return a random action.
		"""
		raiseNotDefined()

class ReinforcementAgent(ValueEstimationAgent):
	"""TODO: need to add the ability to oberve state transitions and update q values"""

	