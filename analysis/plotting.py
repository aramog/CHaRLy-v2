from Subject import *

import matplotlib.pyplot as plt

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
