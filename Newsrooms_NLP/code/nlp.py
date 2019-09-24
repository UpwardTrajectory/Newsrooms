import os
import sqlite3
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

# Downloads the NLTK stopword corpus if not already downloaded
try:
	nltk.download('stopwords')
except Exception as e:
	print(e)
    #nltk.data.fine('corpora/stopwords')


def process_document(text):
	"""
	Processes a text document by coverting all words to lower case,
	tokenizing, removing all non-alphabetical characters,
	and stemming each word.
	Args:
		text: A string of the text of a single document.
	Returns:
		A list of processed words from the document.
	"""
	# Convert words to lower case
	text = text.lower()

	# Tokenize corpus and remove all non-alphabetical characters
	tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(text)

	# Remove stopwords
	stop_words = nltk.corpus.stopwords.words('english')
	set_stopwords = set(stop_words)
	stopwords_removed = [token for token in tokens if not token in set_stopwords]

	# Stem words
	stemmer = nltk.stem.SnowballStemmer('english')
	stemmed = [stemmer.stem(word) for word in stopwords_removed]

	# Return list of processed words
	return stemmed


def load_labels(data_dir):
	"""
	Returns a dictionary = {unique_label: [titles]}
	"""
	conn = sqlite3.connect('articles_db.db')
	cur = conn.cursor()
	categories = dict()
	for i in range(62):
		cur.execute('SELECT id from articles where category=' + str(i))
		data = cur.fetchall()
		if len(data) != 0:
			categories[i] = [tup[0] for tup in data]
	return categories


def load_articles(data_dir):
	"""
	"""
	conn = sqlite3.connect('articles_db.db')
	cur = conn.cursor()
	categories = dict()
	cur.execute('SELECT title,content from articles')
	data = cur.fetchall()
	return data


def classify_documents(topics, labels):
	pass


def cluster_documents():
	pass


def load_all(data_dir):
    """Given a string of the data directory, return a tuple:
    (
    'corpus', #-> [(title1, article1), (title2, article2), ...]
    'labels'  #-> {unique_label: [titles]}
    )
    Typical usage:
    corpus, labels = load_all(data_dir)
    """
    corpus = load_articles(data_dir)
    labels = load_labels(data_dir)
    return (corpus, labels)


def print_top_words(model, feature_names, n_top_words):
    """Print the most important words that distinguish each Topic from the rest.
    """
    print('Topics in:')
    print(str(model))
    for topic_idx, topic in enumerate(model.components_):
        message = f"----------  Topic #{topic_idx}:  ----------\n" 
        message += " ".join(
            [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        )
        print(message)
    print()


# Run using 'python nlp.py' or 'python nlp.py <PATH_TO_BBC_DIRECTORY>'
# to manually specify the path to the data.
# This may take a little bit of time (~30-60 seconds) to run.
if __name__ == '__main__':
	# data_dir = '/course/cs1951a/pub/nlp/bbc/data' if len(sys.argv) == 1 else sys.argv[1]
	data_dir = os.path.join(os.getcwd(), 'articles_db.db')
	load_all(data_dir)