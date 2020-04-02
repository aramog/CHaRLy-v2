"""File to store the agent environment interaction loop."""
from agent import *
from env import Charly
from task_logic import *

agent = RandomAgent()
env = Charly(*task_params(transfer = "high"))
#initializes both the agent and environment
inital_state = env.reset()
agent.reset(inital_state)
#TODO: sets up the data collecting variables
#runs the agent environment interaction loop
while not env.finished():
	#agent first takes an action
	action = agent.policy()
	#environment reacts to action
	next_state, reward = env.step(action)
	#agent observes that reaction
	agent.observe(next_state, reward)
	#TODO: collects all the data from this trial
	if reward != 0:
		print(reward)