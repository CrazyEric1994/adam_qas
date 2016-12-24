import math
from textblob import TextBlob as tb
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

documents = []
path = "home/amit/IdeaProjects/adam_qas/corpora/clustering_docs/"

document1 = open("/home/amit/IdeaProjects/adam_qas/corpora/clustering_docs/a1.txt","r").read()
document1 = document1.lower()
doc1_tok = nltk.word_tokenize(document1)


#print(doc1_tok)
filtered_word_list = doc1_tok[:]

for word in doc1_tok:
    if word in stopwords.words('english'):
        filtered_word_list.remove(word)
print(filtered_word_list)
newdoc_1 = ' '.join(filtered_word_list)
print(newdoc_1)

document1 = tb(newdoc_1)

bloblist = [document1]

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:10]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
