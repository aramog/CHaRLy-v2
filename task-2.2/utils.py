from psychopy import event, visual
import time
import json


def keyHandler(keyMap):
	"""Given a keyMap, returns the number corresponding to the letter pressed.
	Also returns the scalar reaction time for pressing that key"""
	keys = list(keyMap.keys())
	keys.append("1") #we set 1 to be the unique exit key
	#Now wait for the user input
	start = time.time()
	key = event.waitKeys(keyList = keys)
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

def showPreMachineScreen(win, machine, holdTime = 20):
	"""Screen to show the participants before they use a new machine. Will
	show a picture of the machine and the keys that control it."""
	message = visual.TextStim(
		win = win,
		text = "This is the new machine:",
		pos = [0, 200],
		color = [-1, -1, -1],
		bold = True)
	message.draw()
	machineStim = visual.ImageStim(
		win = win,
		image = machine.assets["machine"],
		pos = [0, 0])
	machineStim.draw()
	keys = (machine.keys[0], machine.keys[1], machine.keys[2], machine.keys[3])
	keyStim = visual.TextStim(
		win = win,
		text = "It is controlled by keys: %s, %s, %s, %s"%keys,
		pos = [0, -200],
		color = [-1, -1, -1],
		bold = True)
	keyStim.draw()
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
