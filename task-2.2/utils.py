from psychopy import event, visual
import time
import json

MAX_WAIT_TIME = 5


def keyHandler(keyMap):
	"""Given a keyMap, returns the number corresponding to the letter pressed.
	Also returns the scalar reaction time for pressing that key"""
	keys = list(keyMap.keys())
	keys.append("1") #we set 1 to be the unique exit key
	#Now wait for the user input
	start = time.time()
	key = event.waitKeys(MAX_WAIT_TIME, keyList = keys)
	if not key:
		return -1, -1
	rt = time.time() - start
	if (key[0] in keyMap):
		return keyMap[key[0]], rt #gets the number corresponding to this key
	elif (key[0] == "1"):
		#TODO: instead of exiting here, should send an exit signal up to task so that it can save data
		exit("Exit key pressed")
	return -1, rt

def makeJson(blocks, fileName):
	"""Takes a list of block objects and saves a 
	json file with all the data."""
	"""res = []
				for block in blocks:
					data = block.getData()
					res.append(data)
				#saves as json"""
	with open(fileName, 'w') as outfile:
		json.dump(blocks, outfile, sort_keys=True, indent=4, separators=(',', ': '))

def showStarSwitchScreen(win, starImg):
	"""Given a psychopy window, prints a message on the screen saying that the goal star is now changing."""
	message = visual.TextStim(
		win = win,
		text = "The goal star is now:",
		pos = [0, 200],
		color = [-1, -1, -1],
		bold = True)
	message.draw()
	star = visual.ImageStim(
		win = win,
		image = starImg,
		pos = [0, 0])
	star.draw()
	win.flip()

def showBreakScreen(win, breakTime = 60):
	"""Given a psychopy window, shows participants a break screen for 1m."""
	message = visual.TextStim(
		win = win,
		text = "Break time! The machine will now switch, so that means all new rules, stars, and parts.",
		pos = [0, 0],
		color = [-1, -1, -1],
		bold = True)
	message.draw()
	win.flip()
	time.sleep(breakTime)

def showPreMachineScreen(win, machine):
	"""Screen to show the participants before they use a new machine. Will
	show a picture of the machine and the keys that control it."""
	message = visual.TextStim(
		win = win,
		text = "This is the new machine:",
		pos = [-300, 200],
		color = [-1, -1, -1],
		bold = True)
	message.draw()
	machineStim = visual.ImageStim(
		win = win,
		image = machine.assets["machine"],
		pos = [-300, 0])
	machineStim.draw()
	keys = (machine.keys[0], machine.keys[1], machine.keys[2], machine.keys[3])
	if keys[0] == "u":
		hand = "right"
	else:
		hand = "left"
	keyStim = visual.TextStim(
		win = win,
		text = "It is controlled by keys: %s, %s, %s, %s with the %s hand, as shown below:"%(*keys, hand),
		pos = [300, 200],
		color = [-1, -1, -1],
		bold = True)
	keyStim.draw()
	if hand == "right":
		image = "./assets/rightHand.png"
	else:
		image = "./assets/leftHand.png"
	handStim = visual.ImageStim(
		win = win,
		image = image,
		pos = [300, 0])
	handStim.size = [handStim.size[0] * .1, handStim.size[1] * .1]
	handStim.draw()
	continueStim = visual.TextStim(
		win = win,
		text = "[Press any key when you're ready]",
		pos = [0, -300],
		color = [-1, -1, -1])
	continueStim.draw()
	win.flip()
	event.waitKeys()

def showPostMachineScreen(win, machine, holdTime = 10):
	"""Screen to show after they have used a machine. Only used if there is another machine coming."""
	pointStim = visual.TextStim(
		win = win,
		text = "Great job! You unlocked %d stars using the last machine."%machine.points,
		pos = [0, 100],
		color = [-1, -1, -1],
		bold = True)
	pointStim.draw()

	breakStim = visual.TextStim(
		win = win,
		text = "You will now have a 1 minute break, after which you'll be able to control a new machine.",
		pos = [0, -100],
		color = [-1, -1, -1],
		bold = True)
	breakStim.draw()
	win.flip()
	time.sleep(holdTime)

def randomizeMachines(machines, keys1, keys2, subjID):
	"""Given a subject id mod 4, we have the 4 following cases:
	0: highTrans/keys1 then lowTrans/keys2
	1: lowTrans/keys1 then highTrans/keys2
	2: highTrans/keys2 then lowTrans/keys1
	3: lowTrans/keys3 then highTrans/keys1"""
	subjID = subjID % 4
	#sets the 2 cases for keys and sets the keyMap
	if subjID == 0 or subjID == 3:
		machines[0].keys = keys1
		machines[1].keys = keys2
	else:
		machines[1].keys = keys1
		machines[0].keys = keys2
	machines[0].setKeyMap()
	machines[1].setKeyMap()
	#reorders the machines
	print(machines[1].keys)
	if subjID == 0 or subjID == 2:
		return machines
	else:
		return [machines[1], machines[0]]

def betweenBlockScreen(win, machine1, machine2):
	"""Shows the following 3 screens in between blocks of the task:
	screen1: says that the block is now over and how many stars unlocked.
	screen2: break screen
	screen3: premachine screen"""
	#screen1
	showPostMachineScreen(win, machine1, 10)
	#screen2
	breakStim = visual.TextStim(
		win = win,
		text = "1 minute break.",
		pos = [0, 0],
		color = [-1, -1, -1],
		bold = True)
	breakStim.draw()
	win.flip()
	time.sleep(60)
	#screen3
	showPreMachineScreen(win, machine2)

def showEndScreen(win, totalPoints):
	text = "Great job! You unlocked a total of %d stars. \n \n Thank you for participating and have a nice day!"%totalPoints
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 0],
		color = [-1, -1, -1],
		bold = True,
		height = 30)
	textStim.draw()
	win.flip()
	time.sleep(30)

def showSlowScreen(win):
	"""Shows a screen when they take too long to respond."""
	text = "You took too long to respond that last trial. Please be faster in the future. \n \n Press any key when you're ready to start again"
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, 0],
		color = [-1, -1, -1],
		bold = True,
		height = 30)
	textStim.draw()
	win.flip()
	event.waitKeys()


