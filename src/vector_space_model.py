
import os
import nltk
from nltk.stem.snowball import SnowballStemmer
import re
from nltk.corpus import stopwords

stemmer = SnowballStemmer("english")                                            # Applied Stemming


class TfIdf:
    def __init__(self):
        self.weighted = False
        self.documents = []
        self.corpus_dict = {}

    def add_document(self,  doc_name,  list_of_words):                      # building a dictionary
        doc_dict = {}
        for w in list_of_words:
            doc_dict[w] = doc_dict.get(w,  0.) + 1.0
            self.corpus_dict[w] = self.corpus_dict.get(w,  0.0) + 1.0

        length = float(len(list_of_words))                                  # normalizing the dictionary
        for k in doc_dict:
            doc_dict[k] = (doc_dict[k] / length)
        self.documents.append([doc_name,  doc_dict])                        # add the normalized document to the corpus

    def similarities(self,  list_of_words):                               # building the query dictionary
        query_dict = {}
        for w in list_of_words:
            query_dict[w] = query_dict.get(w,  0.0) + 1.0

        # normalizing the query
        length = float(len(list_of_words))
        for k in query_dict:
            query_dict[k] = (query_dict[k] / length)

        # computing the list of similarities
        sims = []
        for doc in self.documents:
            score = 0.0
            doc_dict = doc[1]
            for k in query_dict:
                if k in doc_dict:
                    score += (query_dict[k] / self.corpus_dict[k]) + (doc_dict[k] / self.corpus_dict[k])
            sims.append([doc[0],  score])

        return sims

documents = ['p1.txt', 'p2.txt', 'p3.txt', 'p4.txt', 'p5.txt']                 # Temporary Data Structures
file_content = [1, 2, 3, 4, 5]
tokens = file_content
titles = ['Barack H Obama', 'Donald J Trump', 'Narendra D Modi', 'Sharad Pawar', 'Vladimir Putin ']
doc_len = len(documents)
key = []
filtered = []
stemmed = []


q = input("Q.").strip()                                                # Accepting Question from user
q = q.lower()
q_tok = nltk.word_tokenize(q)                                          # Tokenizing it
question_stemmed = []
for item in q_tok:
    question_stemmed.append(stemmer.stem(item))                        # Stem it
print(question_stemmed)

obj = TfIdf()                                                           # Object of Class

path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src",  "/corpora/clustering_data/")
pattern = '([[])\w+]'

for i in range(0, doc_len):
    file_content[i] = open(path+documents[i]).read()                                # read content
    file_content[i] = file_content[i].lower()                                       # lower them
    file_content[i] = re.sub(pattern, '', file_content[i])                          # remove citations
    tokens[i] = nltk.word_tokenize(file_content[i])                                 # tokenize the document
    filtered = [w for w in tokens[i] if not w in stopwords.words('english')]        # remove stopwords
    # print(filtered)                                                               # print tokens
    for item in filtered:
        stemmed.append(stemmer.stem(item))
    # print(stemmed)
    obj.add_document(titles[i], stemmed)                                           # sent it to similarity checking

print(obj.similarities(question_stemmed))
