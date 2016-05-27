import sys

#will be a dictionary with tuples as keys, integers as values
pairs = dict()

for line in sys.stdin:
	#string line, break into words
	line = line.strip()
	words = line.split(" ")

	#skip this line if there are fewer than two words on into
	if len(words) < 2:
		continue

	#iterate from 0 up to the length of the list minus one
	for i in range(len(words) - 1):
		pair = tuple(words[i:i+2])
		if pair in pairs:
			pairs[pair] += 1
		else:
			pairs[pair] = 1

# print out pairs
for pair in pairs.keys():
	count = pairs[pair]
	if count > 1: #only rint pairs that occur more than onece
		print ' '.join(pair) + ': ' + str(count)