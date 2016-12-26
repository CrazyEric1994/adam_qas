import time
import os
import nltk
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer



start_time = time.time()
documents = []
path = '/home/amit/IdeaProjects/adam_qas/corpora/clustering_docs/'
class amit:

    def fun(self):
        for filename in os.listdir(path):
            documents.append(filename)
        for i in documents:
            with open(path+i, 'r') as text_file:
                text = text_file.read()
                lowers = text.lower()
                #print(text)
                text = text.split(".")
                print(text)
                new_term_freq_matrix = TfidfVectorizer.transform(self,raw_documents=text,copy=True)
                print (TfidfVectorizer.vocabulary_)
                print (new_term_freq_matrix.todense())

amit().fun()
