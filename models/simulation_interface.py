"""File to store the agent environment interaction loop."""
from flat_agent import *
from env import Charly
from task_logic import *

agent = FlatAgent()
env = Charly(*task_params(transfer = "high"), seqLength = 300)
#initializes both the agent and environment
inital_state = env.reset()
agent.reset(inital_state)
#TODO: sets up the data collecting variables
rewards = []
trial = 0
#runs the agent environment interaction loop
while not env.finished():
	#agent first takes an action
	action = agent.policy()
	#environment reacts to action
	next_state, reward = env.step(action)
	#agent observes that reaction
	agent.observe(next_state, reward)
	#TODO: collects all the data from this trial
	trial += 1
	if trial % 4 == 0:
		#means we've gone through 4 key presses, so record reward
		rewards.append(reward)
		