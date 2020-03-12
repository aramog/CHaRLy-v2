from StarMachine import *
from psychopy import visual
from utils import *
import numpy as np

WINDOW_SIZE = [1600, 800]

win = visual.Window(
	size = WINDOW_SIZE,
	color = [1, 1, 1],
	units = "pix"
)
win.mouseVisible = False
data = dict()
highTransfer = highTransferStarMachine(win, lenGoalSeq = 25)
lowTransfer = lowTransferStarMachine(win, lenGoalSeq = 25)
machines = [highTransfer, lowTransfer]
#randomizes the order of blocks
np.random.shuffle(machines)

#runs the blocks, with a break in between
for i in range(len(machines)):
	machines[i].block.runBlock()
	if machines[i].MACHINE_TYPE == "high":
		data["high_transfer"] = machines[i].block.getData()
	else:
		data["low_transfer"] = machines[i].block.getData()
	if i == len(machines) - 1: break #don't want to show break screen at the end
	showBreakScreen(win, 60)

makeJson(data, "data/test.json")
