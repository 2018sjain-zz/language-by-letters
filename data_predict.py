import numpy as np
import re

en = [np.load('npy_percents/english_one.npy'), 
	  np.load('npy_percents/english_two.npy'), 
	  np.load('npy_percents/english_three.npy'),
	  'english']
es = [np.load('npy_percents/spanish_one.npy'), 
	  np.load('npy_percents/spanish_two.npy'), 
	  np.load('npy_percents/spanish_three.npy'),
	  'spanish']
fr = [np.load('npy_percents/french_one.npy'), 
	  np.load('npy_percents/french_two.npy'), 
	  np.load('npy_percents/french_three.npy'),
	  'french']
de = [np.load('npy_percents/german_one.npy'), 
	  np.load('npy_percents/german_two.npy'), 
	  np.load('npy_percents/german_three.npy'),
	  'german']

def clean(word):
	return re.sub('[^a-zA-Z\n\.]', ' ', word)

def num(letter):
	letter = letter.lower()
	if letter == ' ': return 0
	return ord(letter) - 96

def percents(vals):
	total = sum(vals)
	if total == 0: total = 1 
	percents = [round((var/total)*100, 2) for var in vals]
	return percents

def one_chance(letter, lang):
	return lang[0][num(letter)]
def two_chance(letter_a, letter_b, lang):
	return lang[1][num(letter_a)][num(letter_b)]
def three_chance(letter_a, letter_b, letter_c, lang):
	return lang[2][num(letter_a)][num(letter_b)][num(letter_c)]

def calculate(user_input, lang, a, b, c):
	one_prob = 1
	two_prob = 1
	three_prob = 1
	for letter in user_input:
		one_prob *= one_chance(letter, lang)
	for letter in range(len(user_input)-1):
		two_prob *= two_chance(user_input[letter], user_input[letter+1], lang)
	for letter in range(len(user_input)-2):
		three_prob *= three_chance(user_input[letter], user_input[letter+1], user_input[letter+2], lang)
	return (a*one_prob) + (b*two_prob) + (c*three_prob)

user_input = 'buen tiempo'
user_input = clean(user_input.lower())
print('input: ' + user_input + '\n\n' + 'results:' )

results = []
languages = [en, es, fr, de]
for lang in languages:
	prob = calculate(user_input, lang, 2, 12, 4)
	results.append((prob, lang[3]))

sort = sorted(results, reverse = True, key=lambda tup: tup[0])
percents = percents([val[0] for val in sort])
for x in range (len(sort)):
	print(sort[x][1] + ": " + str(percents[x]) + '%')

#2, 12, 4