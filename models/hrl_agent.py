from flat_agent import *

class HRL_Agent(FlatAgent):
	def __init__(self, middle_seqs, alpha=.1, epsilon=.1, gamma=.8):
		self.middle_seqs = middle_seqs
		self.in_seq = False #true when agent is in the middle of executing a middle seq option
		FlatAgent.__init__(self, alpha, epsilon, gamma)

	def policy(self):
		#first checks if in the middle of executing a sequence
		if self.in_seq:
			self.in_seq = False #so we don't do this twice in a row
			return self.middle_seqs[self.last_action][1] #returns the second item in the current sequence
		#otherwise chooses the best middle seq to execute using
		self.in_seq = True
		action = FlatAgent.policy(self) #mechanics of choosing a middle layer item are exactly the same as the flat agent
		return action

	def observe(self, state, reward):
		"""Just a wrapper for the flat agent observe method that acts when not in 
		the middle of a item seq."""
		if self.in_seq:
			pass
		else:
			FlatAgent.observe(self, state, reward)

	def featurize(self, state):
		"""To make all other parts of the flat agent work here, just need
		to write a new featurizer that ignores certain parts of the state."""
		featurized_state = FlatAgent.featurize(self, state)
		#now needs to remove all the key information from the state
		hrl_state = (featurized_state[1], featurized_state[2], featurized_state[3])
		return hrl_state