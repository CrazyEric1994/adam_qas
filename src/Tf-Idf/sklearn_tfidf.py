
import os
import nltk
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


documents = []
corpus_path = os.path.dirname(os.path.realpath(__file__))
corpus_path = corpus_path.replace("/src/Tf-Idf", "/corpora/")
path = corpus_path+'clustering_docs/'


for filename in os.listdir(path):
    documents.append(filename)
for i in documents:
    with open(path+i, 'r') as text_file:
        text = text_file.read()
        lowers = text.lower()
        #print(text)
        #text = text.split(".")
        #print(text)
        new_term_freq_matrix = TfidfVectorizer.transform(text, copy=True)
        print(TfidfVectorizer.vocabulary_)
        print(new_term_freq_matrix.todense())
