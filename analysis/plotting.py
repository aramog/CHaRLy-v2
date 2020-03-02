from Subject import *

import matplotlib.pyplot as plt
import numpy as np

def get_subj(num):
	"""Returns the subject object associated with num."""
	path = "data/subj" + str(num) + ".json"
	return Subject(path)

def plot_item_seq(block, axs = plt, xtick_spacing = 4):
	if axs is plt:
		plt.figure(figsize=(15,5))

	for i in range(len(block) * 4):
		trial_num = i // 4
		key_num = i % 4
		trial = block[trial_num]

		#check for middle layer
		if key_num % 2 == 1:
			#means we can unlock a m.l. item
			presses = [trial.keys[key_num - 1], trial.keys[key_num]]
			item = int(check_unlock(presses, trial.rules[0]))
			if item > -1:
				if item in trial.rules[1][str(trial.goal_star)]:
					axs.scatter(i / 4, 1, marker = 'o', color = "green")
				else:
					axs.scatter(i / 4, 1, marker = 'o', color = "red")
			else:
				axs.scatter(i / 4, 1, marker = '.', color = "blue")

		#check for high layer
		if key_num == 3:
			presses1 = [trial.keys[0], trial.keys[1]]
			item1 = int(check_unlock(presses1, trial.rules[0]))

			presses2 = [trial.keys[2], trial.keys[3]]
			item2 = int(check_unlock(presses2, trial.rules[0]))

			ml_seq = [item1, item2]
			high_item = int(check_unlock(ml_seq, trial.rules[1]))

			if high_item > -1:
				if high_item == trial.goal_star:
					axs.scatter(i / 4, 2, marker = 'o', color = "green")
				else:
					axs.scatter(i / 4, 2, marker = 'o', color = "red")
			else:
				axs.scatter(i / 4, 2, marker = '.', color = "blue")

	if axs is plt:
		plt.title('Items Unlocked by Trial by Layer')
		plt.xlabel('Trial')
		plt.xticks(range(0, len(block), xtick_spacing))
		plt.ylabel('Layer')
		plt.show()


def check_unlock(presses, rules):
	"""
	presses: two item list of keystrokes
	rules: dict of layer rules
	return: item id of layer item unlocked or
	-1 if no item was unlocked
	"""
	for key, value in rules.items():
		if value == presses:
			return key
	return -1

def item_seq_rts(block):
	"""Plots a bar for average rt for start seq,
	finish seq, and no seq key strokes.
	start seq: first stroke in a two key combo to unlock
	a middle layer item.
	finish seq: second stroke in a two ""
	no seq: none of the above two."""
	avgs, sem = seq_rts(block)
	plt.bar(range(3), avgs,
		tick_label=["Start Sequence", "Finish Sequence", "No Sequence"], yerr = sem)
	plt.ylabel("Average RT")
	plt.show()

def seq_rts(block):
	"""Returns the average reaction time for each of the
	types of key sequences."""
	no, start, finish = [], [], []
	for trial in block:
		for i in range(4):
			seq = seq_type(trial, i)
			if seq == 0:
				#means start seq
				start.append(trial.reaction_times[i])
			elif seq == 1:
				#finish seq
				finish.append(trial.reaction_times[i])
			else:
				#non seq
				no.append(trial.reaction_times[i])
	avgs = [np.mean(start), np.mean(finish), np.mean(no)]
	root_n = np.sqrt(len(block))
	sem = [np.std(start) / root_n, np.std(finish) / root_n, np.std(no) / root_n]
	return avgs, sem

def seq_type(trial, i):
	"""Returns the key press seq type where
	0: finish seq
	1: start seq
	2: non seq"""
	rules = trial.rules[0]
	rules = [rule for key, rule in rules.items()]
	if i == 0 or i == 2:
		#means we only have start seq
		seq = [trial.keys[i], trial.keys[i + 1]]
		if seq in rules:
			return 0
		else:
			return 2
	else:
		#only finish seq
		seq = [trial.keys[i - 1], trial.keys[i]]
		if seq in rules:
			return 1
		else:
			return 2
