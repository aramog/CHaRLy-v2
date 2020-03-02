from StarMachine import *
from psychopy import visual
from utils import *

WINDOW_SIZE = [1600, 800]

win = visual.Window(
	size = WINDOW_SIZE,
	color = [1, 1, 1],
	units = "pix"
)
win.mouseVisible = False
data = dict()
highTransfer = highTransferStarMachine(win, lenGoalSeq = 15)
lowTransfer = lowTransferStarMachine(win, lenGoalSeq = 15)

highTransfer.block.runBlock()
data["high transfer"] = highTransfer.block.getData()
lowTransfer.block.runBlock()
data["low transfer"] = lowTransfer.block.getData()

makeJson(data, "data/test.json")
