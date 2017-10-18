import numpy as np

def num(letter):
	letter = letter.lower()
	if letter == ' ': return 0
	return ord(letter) - 96

def percents(vals):
	total = sum(vals)
	if total == 0: total = 1 
	percents = [(var/total) for var in vals]
	return percents

files = [['ENGLISH/english_clean.txt', 'english'], ['SPANISH/spanish_clean.txt', 'spanish'],
		 ['FRENCH/french_clean.txt', 'french'], ['GERMAN/german_clean.txt', 'german']]

for file in files:
	one = [0 for x in range (27)]
	two = [[0 for x in range (27)] for x in range (27)]
	three = [[[0 for x in range (27)] for x in range (27)] for x in range (27)]
	data = open(file[0], 'r', encoding = 'utf8').read()
	for letter in range(len(data)-2):
		cur = num(data[letter])
		nex = num(data[letter + 1])
		fur = num(data[letter + 2])
		one[cur] += 1
		two[cur][nex] += 1
		three[cur][nex][fur] += 1

	one = percents(one)
	for array in range(len(two)):
		two[array] = percents(two[array])
	for value in range(len(three)):
		for array in range(len(three[value])):
			three[value][array] = percents(three[value][array])

	np.save(file[1]+'_one', one)
	np.save(file[1]+'_two', two)
	np.save(file[1]+'_three', three)