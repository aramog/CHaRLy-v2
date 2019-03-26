from tutorial import *
from Block import *

#TASK SWITCHES
FULL_SCREEN = False
WINDOW_SIZE = [800, 800] #if not full screen, will use this window size
RUN_TUTORIAL = False #whether to show the tutorial, false for testing

#creates window for the task
win = visual.Window(
	size = WINDOW_SIZE,
	fullscr = FULL_SCREEN, 
	color = [1, 1, 1],
	units = "pix")

if RUN_TUTORIAL:
	runTutorial(win)

block = HighTransferBlock(True, win)
block.runBlock()

win.close()