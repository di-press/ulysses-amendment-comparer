import nltk

from model.savoy import Savoy

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('rslp')

from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer
from string import punctuation
from unicodedata import normalize

def _remove_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def preprocess(txt):
    txt = str(txt)
    txt = _remove_acentos(txt)
    stopwords = nltk.corpus.stopwords.words("portuguese")
    stopwords.extend(list(punctuation))

    stemmer = Savoy()
    tokenizer = RegexpTokenizer('\w+')
    terms = tokenizer.tokenize(txt.lower())
    terms = [stemmer.stem(word) for word in terms if word not in stopwords]

    ngram = []
    ngram_1 = list(ngrams(terms, 1))
    ngram_2 = list(ngrams(terms, 2))
    for w in ngram_1:
        ngram.append(w[0])

    for w in ngram_2:
        string = w[0] + " " + w[1]
        ngram.append(string)

    return ngram