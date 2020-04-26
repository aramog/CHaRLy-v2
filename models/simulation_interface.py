"""File to store the agent environment interaction loop."""
from flat_agent import *
from agent import RandomAgent
from hrl_agent import *
from env import Charly
from task_logic import *

def main(seqLength, agent = FlatAgent(), env = None):
	agent = agent
	#agent = FlatAgent()
	if not env:
		env = Charly(*task_params(transfer = "none"), seqLength = seqLength)
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
			if _ % 2 == 0:
				print(agent.last_action)
			#environment reacts to action
			next_state, reward = env.step(action)
			#agent observes that reaction
			agent.observe(next_state, reward)
		rewards.append(reward)
	return rewards, agent

if __name__ == "__main__":
	params = task_params(transfer = "none")
	env = Charly(*params, seqLength = 1000)
	rules = params[0]
	middle_seqs = rules[0][0]
	hrl_agent = FlatAgent()
	r, a  = main(0, hrl_agent, env)