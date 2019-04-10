from psychopy import visual, event

def drawBlankTask(win):
	"""Draws a blank template for a trial. This includes drawing
	the machine, both stars, and the key history box."""
	machine = visual.ImageStim(
		win = win,
		image = "assets/machine.jpg")
	machine.draw()

	window_cover = visual.Rect(
		win = win,
		fillColor = [1, 1, 1],
		pos = [-35, -40],
		width = 135,
		height = 65)
	window_cover.draw()

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

def blankScreen(win):
	"""Wipes the screen inbetween trials."""
	win.flip()

def drawGear(win, itemsOnScreen):
	"""Draws the gear stimulus."""
	if itemsOnScreen == 0:
		x = -60
	else:
		x = 0
	gear = visual.ImageStim(
		win = win,
		image = "assets/gear.jpg",
		pos = [x, -40])
	gear.size = [gear.size[0] * .7, gear.size[1] * .7]
	gear.draw()

def drawLight(win, itemsOnScreen):
	"""Draws the light stimulus."""
	if itemsOnScreen == 0:
		x = -60
	else:
		x = 0
	light = visual.ImageStim(
		win = win,
		image = "assets/light.jpg",
		pos = [x, -40])
	light.size = [light.size[0] * .7, light.size[1] * .7]
	light.draw()

def drawPower(win, itemsOnScreen):
	"""Draws the power stimulus."""
	if itemsOnScreen == 0:
		x = -60
	else:
		x = 0
	power = visual.ImageStim(
		win = win,
		image = "assets/power.jpg",
		pos = [x, -40])
	power.size = [power.size[0] * .07, power.size[1] * .07]
	power.draw()

def drawFan(win, itemsOnScreen):
	"""Draws the fan stimulus."""
	if itemsOnScreen == 0:
		x = -60
	else:
		x = 0
	fan = visual.ImageStim(
		win = win,
		image = "assets/fan.jpg",
		pos = [x, -40])
	fan.size = [fan.size[0] * .1, fan.size[1] * .1]
	fan.draw()


def highlightOrangeStar(win):
	"""Draws a box around the orange star to indicate
	the particpant should try to unlock that star."""
	orange_star = visual.ImageStim(
		win = win,
		image = "assets/orange-star.png",
		pos = [0, 300])
	orange_star.draw()
	highlightBox = visual.Rect(
		win = win,
		width = 110,
		height = 110,
		pos = [0, 300],
		lineColor = [-1, -1, -1],
		lineWidth = 5)
	highlightBox.draw()

def unlockOrangeStar(win):
	"""Draws a box around the orange star and fills it
	green to indicate it has been unlocked."""
	#TODO: Make this unlock towards the bottom left of the machine
	orange_star = visual.ImageStim(
		win = win,
		image = "assets/orange-star.png",
		pos = [-100, -150])
	orange_star.draw()

def highlightBlackStar(win):
	"""Draws a box around the black star to indicate
	the particpant should try to unlock that star."""
	black_star = visual.ImageStim(
		win = win,
		image = "assets/black-star.png",
		pos = [0, 300])
	black_star.draw()
	highlightBox = visual.Rect(
		win = win,
		width = 110,
		height = 110,
		pos = [0, 300],
		lineColor = [-1, -1, -1],
		lineWidth = 5)
	highlightBox.draw()

def unlockBlackStar(win):
	"""Draws a box around the black star and fills it
	green to indicate it has been unlocked."""
	black_star = visual.ImageStim(
		win = win,
		image = "assets/black-star.png",
		pos = [-100, -150])
	black_star.draw()
	"""
	idea I had to open the front flaps when a star is unlocked.
	hard to make look good so I scrapped it.
	open_screen = visual.Rect(
		win = win,
		fillColor = [1, 1, 1],
		width = 90,
		height = 40,
		pos = [-38, -110])
	open_screen.draw()
	"""

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
	keys = keys.copy()
	if (keys and type(keys[0]) == int):
		#need to convert to letters
		keyMap = {1: "d", 2: "f", 3: "j", 4: "k", -1: "NA"}
		for i in range(len(keys)):
			keys[i] = keyMap[keys[i]]
	keyStims = []
	for i in range(len(keys)):
		#create the text
		if keys[i] != "NA":
			keyText = visual.ImageStim(
				win = win,
				image = "assets/" + keys[i] + ".png",
				pos = [-95 + i*60, -250])
			keyText.size = [keyText.size[0] * .25, keyText.size[1] * .25]
		else:
			keyText = visual.TextStim(
			win = win,
			text = keys[i].upper(),
			pos = [-95 + i*60, -250],
			color = [-1, -1, -1])
		#add key to the list
		keyStims.append(keyText)

	for keyText in keyStims:
		keyText.draw()

def getKeys():
	keyMap = {"d": 1, "f": 2, "j": 3, "k": 4}
	keys = event.waitKeys()
	if (len(keys) > 1):
		raise Exception("Don't press more than 1 key at a time!")
	if (keys[0] in keyMap):
		return keyMap[keys[0]]
	return -1
