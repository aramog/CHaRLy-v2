from StarMachine import *
from psychopy import visual
from utils import *
import numpy as np
from tutorial import runTutorial

WINDOW_SIZE = [1600, 800]
RUN_TUTORIAL = True
COLLECT_DATA = True
lenGoalSeq = 25

#if collecting data, gets a subject id, otherwise sets it to 0
if COLLECT_DATA:
	subjID = int(input("Subject ID? "))
else:
	subjID = 0

win = visual.Window(
	size = WINDOW_SIZE,
	color = [1, 1, 1],
	units = "pix"
)
win.mouseVisible = False
#runs the tutorial
if RUN_TUTORIAL:
	runTutorial(win)

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
	totalUnlocks += machines[i].points
showEndScreen(win,totalUnlocks)

if COLLECT_DATA:
	makeJson(data, "data/subj_%d.json"%subjID)
