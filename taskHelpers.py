from psychopy import visual, event

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

	key_divide = visual.Line(
		win = win,
		start = [0, -287.5],
		end = [0, -212.5],
		lineColor = [-1, -1, -1],
		lineWidth = 5)
	key_divide.draw()

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
	return highlightBox

def unlockOrangeStar(win):
	"""Draws a box around the orange star and fills it
	green to indicate it has been unlocked."""
	highlightBox = highlightOrangeStar(win)
	highlightBox.fillColor = [-1, 1, -1]
	highlightBox.opacity = .3
	highlightBox.draw()

def highlightBlackStar(win):
	"""Draws a box around the black star to indicate
	the particpant should try to unlock that star."""
	highlightBox = visual.Rect(
		win = win,
		width = 110,
		height = 110,
		pos = [-72, 300],
		lineColor = [-1, -1, -1],
		lineWidth = 5)
	highlightBox.draw()
	return highlightBox

def unlockBlackStar(win):
	"""Draws a box around the black star and fills it
	green to indicate it has been unlocked."""
	highlightBox = highlightBlackStar(win)
	highlightBox.fillColor = [-1, 1, -1]
	highlightBox.opacity = .3
	highlightBox.draw()

def pointCounter(win, points):
	"""Draws a point counter for the given number of 
	points."""
	scoreText = visual.TextStim(
		win = win,
		text = "Points: " + str(points),
		pos = [0, 200],
		color = [-1, -1, -1],
		bold = True)
	scoreText.draw()

def showKeys(win, keys):
	"""Will display all entries of keys (list of chars) in the 
	key stroke box. Assumes first entry of keys was first key 
	pressed in the trial."""
	keyStims = []
	for key in keys:
		#create the text
		keyText = visual.TextStim(
			win = win,
			text = key.upper(),
			pos = [-95, -250],
			color = [-1, -1, -1])
		#move all other text to right
		for keyStim in keyStims:
			keyStim.pos[0] += 60
		#add key to the list
		keyStims.append(keyText)

	for keyText in keyStims:
		keyText.draw()
