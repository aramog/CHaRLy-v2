from psychopy import event
import time
import json


def keyHandler(keyMap):
	"""Given a keyMap, returns the number corresponding to the letter pressed.
	Also returns the scalar reaction time for pressing that key"""
	keys = list(keyMap.keys())
	keys.append(1) #we set 1 to be the unique exit key
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
	res = []
	for block in blocks:
		data = block.getData()
		res.append(data)
	#saves as json
	with open(fileName, 'w') as outfile:
		json.dump(res, outfile, sort_keys=True, indent=4, separators=(',', ': '))