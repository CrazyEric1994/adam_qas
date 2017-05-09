import os
import nltk.data
from corenlp import *
import collections
import difflib
from nltk.corpus import stopwords

commonwords = ["the", "a", "an", "is", "are", "were", "."]

stop = set(stopwords.words('english'))
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src",  "/corpora/data/")

print('Domain:\t Customer relationship management (CRM)')

# q = 'Which instrument is used to measure blood pressure?'           # Sample Question
q = 'What is important aspect of the CRM?'
print('Question: \t', q)
q = q.replace('?', '')

q = q.replace('?', '')
q_tag = nltk.word_tokenize(q)
target = [i for i in q.lower().split() if i not in stop]
# print(target)

article = open(path+'Customer_relationship_management.txt', 'r')
file_data = article.read()
file_data.lower()
sentence = tokenizer.tokenize(file_data)
# print(sentence)

searchstring = ' '.join(q_tag)

'''for i in range(0, len(sentence)):
    # print(sentence[i])
    seq = difflib.SequenceMatcher(None, searchstring, sentence[i])
    d = seq.ratio() * 100
    # print(d, '--->', sentence[i])
'''

conf = 0
for i in range(0, len(sentence)):
    sent_tok = nltk.word_tokenize(sentence[i])
    # print(sent_tok)
    if sent_tok.__contains__(target[0] or target[1] or target[2] or target[3] or target[4] or target[5]):
        print('Answer: \t', sentence[i])