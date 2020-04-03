"""File to store the agent environment interaction loop."""
from flat_agent import *
from agent import RandomAgent
from env import Charly
from task_logic import *

#agent = FlatAgentPseudoReward()
agent = FlatAgent()
env = Charly(*task_params(transfer = "none"), seqLength = 2000)
#initializes both the agent and environment
inital_state = env.reset()
agent.reset(inital_state)
#TODO: sets up the data collecting variables
rewards = []
trial = 0
#runs the agent environment interaction loop
while not env.finished():
	#resets the internal state
	state = env.blank_state()
	agent.update_state(state)
	for _ in range(4):
		#agent first takes an action
		action = agent.policy()
		#environment reacts to action
		next_state, reward = env.step(action)
		#agent observes that reaction
		agent.observe(next_state, reward)
	rewards.append(reward)
