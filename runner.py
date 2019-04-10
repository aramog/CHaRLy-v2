from tutorial import *
from Block import *

from getData import makeJson

#TASK SWITCHES
FULL_SCREEN = False
WINDOW_SIZE = [800, 800] #if not full screen, will use this window size
RUN_TUTORIAL = False #whether to show the tutorial, false for testing
STORE_DATA = False #turn off for testing

if STORE_DATA:
	SUBJ_ID = input("Subject ID? ")

#creates window for the task
win = visual.Window(
	size = WINDOW_SIZE,
	fullscr = FULL_SCREEN, 
	color = [1, 1, 1],
	units = "pix")

if RUN_TUTORIAL:
	runTutorial(win)

blocks = []
blocks.append(HighTransferBlock(True, win))
blocks.append(LowTransferBlock(True, win))

for block in blocks:
	block.runBlock()

if STORE_DATA:
	makeJson(blocks, "data/subj" + SUBJ_ID + ".json")

win.close()
