from psychopy import visual, event

from taskHelpers import *

win = visual.Window(
	size = [800, 800],
	fullscr = False,
	color = [1, 1, 1],
	units = "pix")

drawBlankTask(win)
highlightOrangeStar(win)
win.flip()
event.waitKeys()

drawBlankTask(win)
highlightOrangeStar(win)
win.flip()
event.waitKeys()

drawBlankTask(win)
highlightOrangeStar(win)
drawGear(win)
win.flip()
event.waitKeys()


drawBlankTask(win)
highlightOrangeStar(win)
drawGear(win)
win.flip()
event.waitKeys()


drawBlankTask(win)
highlightOrangeStar(win)
drawGear(win)
drawLight(win)
win.flip()
event.waitKeys()

win.close()

