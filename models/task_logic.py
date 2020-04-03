import numpy as np

def task_params(transfer = "high"):
	#defines the sequences of learning and transfer stars
	learningSequence = [0, 1, 2, 3] *  3
	base = [1, 2]
	np.random.shuffle(base)
	transferSequence = base * 3
	totalSeq = learningSequence + transferSequence
	transferIdx = len(learningSequence)
	#rules
	if transfer == "high":
		middleRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		learningRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		transferRules = {0: (0, 1), 1: (2, 1), 2: (3, 2), 3: (3, 0)}
		rules = [middleRules, learningRules], [middleRules, transferRules]
	elif transfer == "low":
		highRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		learningRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		transferRules = {0: (0, 1), 1: (2, 3), 2: (0, 2), 3: (3, 1)}
		rules = [learningRules, highRules], [transferRules, highRules]
	else:
		highRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		learningRules = {0: (0, 1), 1: (2, 3), 2: (1, 2), 3: (3, 0)}
		rules = [learningRules, highRules], [learningRules, highRules]
	return rules, transferIdx, totalSeq

def update_game_state(curr_state, rules, action):
	def checkLowSeq(state):
		potentialSeq = (state.keys[-2], state.keys[-1]) #picks the last 2 keys pressed
		for item, rule in rules[0].items():
			#iterates over all the low level rules to see if something is unlocked
			if checkSeq(rule, potentialSeq):
				#means we have a valid sequence for this item
				return item
		return -1 #means nothing was unlocked

	def checkHighSeq(itemSeq):
		"""Given a sequence of unlocked items, checks if that forms a valid goal sequence."""
		if len(itemSeq) < 2: 
			#means we didn't unlock 2 middle layer items, so impossible to unlock a goal
			return -1
		for goal, rule in rules[1].items():
			if checkSeq(rule, itemSeq):
				return goal
		return -1 #means we didn't unlock anything

	def checkSeq(rule, seq):
		"""Given a rule and a sequence, returns True only if they match."""
		return rule[0] == seq[0] and rule[1] == seq[1]

	"""Updates the game state based on the given rules and action taken."""
	new_state = curr_state.copy()
	new_state.keys.append(action) #adds the key press to the board state
	if len(new_state.keys) % 2 == 1:
		#means we're at an odd key press and don't need to check for anything
		return new_state
	#otherwise first need to check if another middle layer item is unlocked
	unlocked_item = checkLowSeq(new_state)
	if unlocked_item == -1:
		#means we didn't unlock anything, so we can return
		return new_state
	new_state.items.append(unlocked_item)
	#next checks if a star was unlocked
	new_state.unlockedStar = checkHighSeq(new_state.items)
	return new_state

