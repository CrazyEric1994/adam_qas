import time
import glob
import nltk
import string
from nltk import tokenize
from nltk.corpus import stopwords
import os
from collections import Counter


start_time = time.time()
documents = []
corpus_path = os.path.dirname(os.path.realpath(__file__))
corpus_path = corpus_path.replace("/src/Tf-Idf", "/corpora/")
path = corpus_path+'clustering_docs/'
for filename in os.listdir(path):
    documents.append(filename)
for i in documents:
    #print(i)
    with open(path+i, 'r') as text_file:
        text = text_file.read()
        lowers = text.lower()
        tokens = nltk.word_tokenize(lowers)
        tokens = [''.join(c for c in s if c not in string.punctuation) for s in tokens]
        tokens = [s for s in tokens if s]
        #print(tokens)
        filtered = [w for w in tokens if not w in stopwords.words('english')]
        #print(filtered)
        '''
        for doc in filtered:
            tf = Counter()
            for word in doc.split():
                tf[word] = tf[word] + 1
            print(tf)
        print("-----------------------------------------------------------------------------------------------")
        '''
        tf = Counter()
        for doc in filtered:
            tf [doc] += 1
        print(tf.items())

        def tf(term, document):
            return freq(term, document)

        def freq(term, document):
            return document.split().count(term)

        doc_term_matrix = []
        print( 'Our vocabulary vector is [' + ', '.join(list(filtered)) + ']')



print("------------------------------------------------------------------------------------------------")



