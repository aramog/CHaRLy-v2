from StarMachine import StarMachine
from psychopy import visual

WINDOW_SIZE = [1600, 800]

win = visual.Window(
	size = WINDOW_SIZE,
	color = [1, 1, 1],
	units = "pix"
)
win.mouseVisible = False

sm = StarMachine(win, True)
sm.block.runBlock()