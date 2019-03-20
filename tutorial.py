
from psychopy import visual, event

from taskHelpers import *

win = visual.Window(
	size = [800, 800],
	fullscr = False,
	color = [1, 1, 1],
	units = "pix")

drawBlankTask(win)
highlightBlackStar(win)
pointCounter(win, 0)
win.flip()
event.waitKeys(keyList = ["d"])

drawBlankTask(win)
highlightBlackStar(win)
pointCounter(win, 0)
win.flip()
event.waitKeys(keyList = ["k"])

drawBlankTask(win)
highlightBlackStar(win)
drawGear(win)
pointCounter(win, 0)
win.flip()
event.waitKeys(keyList = ["j"])

drawBlankTask(win)
highlightBlackStar(win)
drawGear(win)
pointCounter(win, 0)
win.flip()
event.waitKeys(keyList = ["f"])


drawBlankTask(win)
unlockBlackStar(win)
drawGear(win)
drawLight(win)
pointCounter(win, 100)
win.flip()
event.waitKeys()

win.close()

def runTutorial(win):
	"""
	Will eventually put body of file here so I can run the tutorial
	from some other script.
	"""
	return None
