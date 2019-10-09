from tutorial import *
from Block import *

from getData import makeJson

#TASK SWITCHES
FULL_SCREEN = True
WINDOW_SIZE = [800, 800] #if not full screen, will use this window size
RUN_TUTORIAL = True #whether to show the tutorial, false for testing
STORE_DATA = True #turn off for testing
LEN_STAR_RUNS = 20 #how long the interval for each star should be
REACTIVE = True #whether env. is reactive

if STORE_DATA:
	SUBJ_ID = input("Subject ID? ")

#creates window for the task
if FULL_SCREEN:
	win = visual.Window(
		fullscr = FULL_SCREEN, 
		color = [1, 1, 1],
		units = "pix")
else:
	win = visual.Window(
		size = WINDOW_SIZE,
		fullscr = FULL_SCREEN, 
		color = [1, 1, 1],
		units = "pix")
win.mouseVisible = False

if RUN_TUTORIAL:
	runTutorial(win)

blocks = []
blocks.append(HighTransferBlock(
	REACTIVE, win, LEN_STAR_RUNS))

for block in blocks:
	block.runBlock()

if STORE_DATA:
	makeJson(blocks, "./data/subj" + SUBJ_ID + ".json")

win.close()
