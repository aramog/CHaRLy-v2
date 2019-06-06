import json

class Subject:
	class Trial:
		def __init__(self, trial_dict):
			self.process_trial(trial_dict)
		
		def process_trial(self, trial_dict):
			self.keys = trial_dict["key_press"]
			self.points = trial_dict["points"]
			self.reaction_times = trial_dict["reaction_times"]
			self.rules = trial_dict["rules"]
			self.goal_star = trial_dict["star"]
			self.unlocked = trial_dict["unlock"]
			self.trial_type = trial_dict["trial_type"]
	
	def __init__(self, json_filename):
		self.data = json.load(open(json_filename))[0]
		self.process_blocks(self.data)

	def process_blocks(self, data):
		"""Processes trial data from a list of dicts."""
		self.blocks = {}
		self.process_trials(data, "learning")
		self.process_trials(data, "pos_transfer")
		self.process_trials(data, "learning2")
		self.process_trials(data, "neg_trans")

	def process_trials(self, data, trial_type):
		"""Adds a new block with key trial_type to self.blocks
		with value as list of all trials with such label."""
		self.blocks[trial_type] = [self.Trial(t) for t in data if t["trial_type"] == trial_type]
