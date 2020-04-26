from StarMachine import *
from psychopy import visual
from utils import *
import numpy as np
from tutorial import runTutorial
import time

WINDOW_SIZE = [1600, 800]
RUN_TUTORIAL = True
COLLECT_DATA = True
FULL_SCREEN = True
lenGoalSeq = 1

subjID = np.random.choice(range(4))

#puts this into a function to be called from the main.py file
def run_task():
	win = visual.Window(
		size = WINDOW_SIZE,
		color = [1, 1, 1],
		units = "pix",
		fullscr = FULL_SCREEN
	)
	win.mouseVisible = False
	#runs the tutorial
	if RUN_TUTORIAL:
		runTutorial(win)
	startTime = time.time() #records the total time it takes to finish the task
	#defines the 2 key sets that the machines will use
	keys1 = ["q", "w", "e", "r"]
	keys2 = ["u", "i", "o", "p"]

	data = dict()
	highTransfer = highTransferStarMachine(win, lenGoalSeq = lenGoalSeq)
	lowTransfer = lowTransferStarMachine(win, lenGoalSeq = lenGoalSeq)
	machines = [highTransfer, lowTransfer]
	#randomizes the order of blocks
	machines = randomizeMachines(machines, keys1, keys2, subjID)
	totalUnlocks = 0
	#runs the blocks, with a break in between
	for i in range(len(machines)):
		machines[i].subjID = subjID
		#works out the prescreen for each machine
		if i == 0:
			showPreMachineScreen(win,machines[0])
		else:
			betweenBlockScreen(win, machines[i - 1], machines[i])
		machines[i].block.runBlock()
		if machines[i].MACHINE_TYPE == "high":
			data["high_transfer"] = machines[i].block.getData()
		else:
			data["low_transfer"] = machines[i].block.getData()
		if i == 0:
			machines[i + 1].pastData = data
		totalUnlocks += machines[i].points
	showEndScreen(win,totalUnlocks)

	totalTime = time.time() - startTIme
	data["total time"] = totalTime

	if COLLECT_DATA:
		makeJson(data, "data/subj_%d.json"%subjID)

if __name__ == "__main__":
	run_task()
