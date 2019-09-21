import os
import sqlite3
import json
# import nltk

# # Downloads the NLTK stopword corpus if not already downloaded
# try:
# 	nltk.data.fine('corpora/stopwords')
# except LookupError:
# 	nltk.download('stopwords')

# from nltk.corpus import stopwords
# from nltk.stem import SnowballStemmer
# from nltk.tokenize import RegexpTokenizer

def return_json():
	"""
	"""
	# data_dir = os.path.join(os.getcwd(), 'articles_db.db')
	conn = sqlite3.connect('articles_db.db')
	cur = conn.cursor()
	categories = dict()
	cur.execute('SELECT id,title,content,category from articles')
	data = cur.fetchall()
	for entry in data:
		cat_num = entry[3]
		if cat_num in categories.keys():
			categories[cat_num].append({'id': entry[0], 'title': entry[1], 'content': entry[2]})
		else:
			categories[cat_num] = [{'id': entry[0], 'title': entry[1], 'content': entry[2]}]
	json_dict = json.dumps(categories)
	return json_dict

# def process_document(text):
# 	"""
# 	Processes a text document by coverting all words to lower case,
# 	tokenizing, removing all non-alphabetical characters,
# 	and stemming each word.
# 	Args:
# 		text: A string of the text of a single document.
# 	Returns:
# 		A list of processed words from the document.
# 	"""
# 	# Convert words to lower case
# 	text = text.lower()

# 	# Tokenize corpus and remove all non-alphabetical characters
# 	tokenizer = RegexpTokenizer(r'\w+')
# 	tokens = tokenizer.tokenize(text)

# 	# Remove stopwords
# 	stop_words = stopwords.words('english')
# 	set_stopwords = set(stop_words)
# 	stopwords_removed = [token for token in tokens if not token in set_stopwords]

# 	# Stem words
# 	stemmer = SnowballStemmer('english')
# 	stemmed = [stemmer.stem(word) for word in stopwords_removed]

# 	# Return list of processed words
# 	return stemmed

if __name__ == '__main__':
	return_json()