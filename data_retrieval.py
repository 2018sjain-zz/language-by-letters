import wikipedia
import re
import unidecode
import numpy as np 

def clean_data(data):
	data = unidecode.unidecode(data).lower()
	data = re.sub('[^a-zA-Z\n\.]', ' ', data)

	data = data.replace('.', ' ')
	data = data.replace('\n', ' ')
	for x in range (100):
	 	data = data.replace("  ", " ")
	return data

languages = [['en', 'english'], ['es','spanish'], ['fr','french'], ['de','german']]

for lang in languages:
	raw = open(lang[1] + '_raw.txt', 'w', encoding='utf8')
	clean = open(lang[1] + '_clean.txt', 'w', encoding='utf8')
	count = 0
	wikipedia.set_lang(lang[0])
	for x in range(2500):
		term = wikipedia.random(pages=1)
		try:
			page = wikipedia.page(term)
			count += 1
		except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e:
			pass
		raw.write(page.content)
		clean.write(clean_data(page.content))
	print(lang[1] + ': ' + str(count))