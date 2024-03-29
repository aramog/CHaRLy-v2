from agent import Agent
import random
import numpy as np
from scipy.special import softmax

class FlatAgent(Agent):
	def __init__(self, alpha = .1, beta = 100, gamma = .8):
		#sets up all the state space and stuff that applies to all agents
		Agent.__init__(self)
		#sets up the Q table, this will be indexed by (state, action) tuples
		self.q_table = dict()
		#sets up the learning and policy params
		self.alpha = alpha #the learning rate
		self.beta = beta #policy noise
		self.gamma = gamma #discount factors
		#defines the prev action to 0 here, just to avoid weird errors
		self.last_action = 0

	def observe(self, state, reward):
		"""Heart of the learner, does TD q learning."""
		#featurizes state so it can be used in the q table
		state = self.featurize(state)
		#defines the prev state and action to use in the update rule
		prev_state = self.curr_state
		prev_action = self.last_action
		#gets the current q value, sets it to 1 if this hasn't been seen before
		if (prev_state, prev_action) in self.q_table:
			prev_value = self.q_table[(prev_state, prev_action)]
		else:
			self.q_table[(prev_state, prev_action)] = 0
			prev_value = 0
		new_state_value = self.get_best(state, what = "value")
		#computes the parts of the update rule
		#TODO: treat the fourth trial as an absorbing state
		RPE = reward + self.gamma * new_state_value - prev_value
		#does the update
		self.q_table[(prev_state, prev_action)] = prev_value + self.alpha * RPE
		#updates the current state
		self.curr_state = state

	def policy(self):
		"""Returns the maximizing action for the q table (given that we're in a current
		state) with prob 1 - epsilon, and a random action with prob eps."""
		"""best_action = self.get_best(self.curr_state, "action")
								if random.random() < self.epsilon:
									action = np.random.choice(self.action_space)
								else:
									action = best_action"""
		action_values = []
		for action in self.action_space:
			if (self.curr_state, action) in self.q_table:
				action_values.append(self.q_table[(self.curr_state, action)])
			else:
				action_values.append(0)
		sm = softmax(-self.beta * np.array(action_values))
		action = np.random.choice(range(len(action_values)), p = sm)
		self.last_action = action
		return action

	def get_best(self, state, what = "action"):
		"""Given a state, return the q value maximizing action or value. If there are no
		q values for the given state, returns a random action."""
		action_values = []
		for action in self.action_space:
			if (state, action) in self.q_table:
				action_values.append(self.q_table[(state, action)])
			else:
				action_values.append(0)
		if what == "action":
			return max(self.action_space, key = lambda a: action_values[a])
		elif what == "value":
			return max(action_values)

	def reset(self, initial_state):
		Agent.reset(self, initial_state)
		self.q_table = dict()

class FlatAgentPseudoReward(FlatAgent):
	"""Same as the flat agent, but gives itself a pseudo reward when an item is seen."""
	def __init__(self, pseudo_reward, alpha=.1, epsilon = .1, gamma = .8):
		self.PSEUDO_REWARD = pseudo_reward
		FlatAgent.__init__(self, alpha, epsilon, gamma)

	def observe(self, state, reward):
		#checks if we need to add a pseudo reward
		if len(state.keys) % 2 == 0:
			#means we need to check for new items
			if len(state.items) > 0 and len(state.keys) == 2:
				#means we unlocked an item, so add a reward
				reward = reward + self.PSEUDO_REWARD
			elif len(state.items) == 2 and len(state.keys) == 4:
				reward = reward + self.PSEUDO_REWARD
		FlatAgent.observe(self, state, reward)

