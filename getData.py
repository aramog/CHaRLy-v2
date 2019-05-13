import json

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