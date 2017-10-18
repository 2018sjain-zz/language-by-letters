import numpy as np

en = [open('dictionary/english_dictionary.txt', 'r').read().split('\n'), 'en']
es = [open('dictionary/spanish_dictionary.txt', 'r').read().split('\n'), 'es']
fr = [open('dictionary/french_dictionary.txt', 'r').read().split('\n'), 'fr']
de = [open('dictionary/german_dictionary.txt', 'r').read().split('\n'), 'de']

words = []
langs = [en, es, fr, de]

for lang in langs:
	np.random.shuffle(lang[0])
	for word in lang[0][:10000]:
		words.append((word, lang[1]))

np.save('words_assigned', words)