import numpy as np

middle_seqs = [(2, 3), (4, 2), (3, 1), (1, 4)]

def gen_learning_seqs(middle_seqs = middle_seqs):
	#generate order of first items
	order1 = [0, 1, 2, 3]
	np.random.shuffle(order1)	
	order2 = [0, 1, 2, 3]
	np.random.shuffle(order2)
	#if any double actions, try again
	if any([a == b for a, b in zip(order1, order2)]):
		return gen_learning_seqs(middle_seqs)
	#make the seqs and return in a dictionary
	seqs = [(a, b) for a, b in zip(order1, order2)]
	#check if any doubles
	return {a: b for a, b in zip(range(1, 5), seqs)}

def gen_neg_transfer(learning_seqs, diag = False):
	#choose 2 high level items to swap
	swaps = np.random.choice(range(1, 5), 2)
	#copy learning dict and get current seqs
	res = learning_seqs.copy()
	s1 = res[swaps[0]]
	s2 = res[swaps[1]]
	#swap the keys according to diag
	if diag:
		temp = s1[0]
		s1 = (s2[1], s1[1])
		s2 = (s2[0], temp)
	else:
		temp = s1[1]
		s1 = (s1[0], s2[1])
		s2 = (s2[0], temp)
	res[swaps[0]] = s1
	res[swaps[1]] = s2
	order1 = [a[0] for a in res.values()]
	order2 = [a[1] for a in res.values()]
	if any([a == b for a, b in zip(order1, order2)]):
		return gen_neg_transfer(learning_seqs, diag)
	if res == learning_seqs:
		return gen_neg_transfer(learning_seqs, diag)
	return res

def print_long(seqs):
	for key, value in seqs.items():
		full_seq = middle_seqs[value[0] - 1], middle_seqs[value[1] - 1]
		full_seq = [a for a in full_seq[0]] + [b for b in full_seq[1]]
		print(full_seq)
	
