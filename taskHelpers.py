from psychopy import visual

def drawBlankTask(win):
	"""Draws a blank template for a trial. This includes drawing
	the machine, both stars, and the key history box."""
	machine = visual.ImageStim(
		win = win,
		image = "assets/machine.jpg")
	machine.draw()

	black_star = visual.ImageStim(
		win = win,
		image = "assets/black-star.jpg",
		pos = [-75, 300])
	black_star.draw()

	orange_star = visual.ImageStim(
		win = win,
		image = "assets/orange-star.jpg",
		pos = [75, 300])
	orange_star.draw()

	key_hist = visual.Rect(
		win = win,
		width = 250,
		height = 75,
		pos = [0, -250],
		lineColor = [-1, -1, -1],
		lineWidth = 5)
	key_hist.draw()

def drawGear(win):
	"""Draws the gear stimulus."""
	gear = visual.ImageStim(
		win = win,
		image = "assets/gear.jpg",
		pos = [-60, -40])
	gear.size = [gear.size[0] * .7, gear.size[1] * .7]
	gear.draw()

def drawLight(win):
	"""Draws the light stimulus."""
	light = visual.ImageStim(
		win = win,
		image = "assets/light.jpg",
		pos = [0, -40])
	light.size = [light.size[0] * .7, light.size[1] * .7]
	light.draw()

def highlightOrangeStar(win):
	"""Draws a box around the orange star to indicate
	the particpant should try to unlock that star."""
	highlightBox = visual.Rect(
		win = win,
		width = 110,
		height = 110,
		pos = [82, 300],
		lineColor = [-1, -1, -1],
		lineWidth = 5)
	highlightBox.draw()