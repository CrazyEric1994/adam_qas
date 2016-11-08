#------------------------Relevant Document Retrieval -------------------------
#---------------------------Imports---------------------------------------
import nltk
import sys
import os
#----------------------------------Class for TF- IDF --------------------
class tfidf:
  def __init__(self):
    self.weighted = False
    self.documents = []
    self.corpus_dict = {}

  def addDocument(self, doc_name, list_of_words):
    # building a dictionary
    doc_dict = {}
    for w in list_of_words:
      doc_dict[w] = doc_dict.get(w, 0.) + 1.0
      self.corpus_dict[w] = self.corpus_dict.get(w, 0.0) + 1.0

    # normalizing the dictionary
    length = float(len(list_of_words))
    for k in doc_dict:
      doc_dict[k] = doc_dict[k] / length

    # add the normalized document to the corpus
    self.documents.append([doc_name, doc_dict])

  def similarities(self, list_of_words):
  # building the query dictionary
    query_dict = {}
    for w in list_of_words:
      query_dict[w] = query_dict.get(w, 0.0) + 1.0

    # normalizing the query
    length = float(len(list_of_words))
    for k in query_dict:
      query_dict[k] = query_dict[k] / length

    # computing the list of similarities
    sims = []
    for doc in self.documents:
      score = 0.0
      doc_dict = doc[1]
      for k in query_dict:
        if k in doc_dict:
          score += (query_dict[k] / self.corpus_dict[k]) + (doc_dict[k] / self.corpus_dict[k])
      sims.append([doc[0], score])

    return sims
#---------------------------End of Class-----------------------------------------------------------------------------

#---------------------Temporary Data structure----------------------------------------------------------------
documents = ['barack.txt','elon.txt','linus.txt']
file_content = [1,2,3]
tokens = [1,2,3]
titles = ['Barack Obama','Elon Musk','Linus Torvalds']
doc_len = len(documents)
key = []

#--------------------Ask Question-----------------------------------------------------------------------------------
#------------------this is temporary cause we need keywords----------------------------------------------

q = raw_input("Q.").strip()
q=q.lower()
q_tok = nltk.word_tokenize(q)
print q_tok
#---------------------------------------------Object of class-----------------------------------------------------
obj = tfidf()	
	
for i in range(0,doc_len):
	file_content[i] = open("Corpus/"+documents[i]).read()
	file_content[i] = file_content[i].lower()
	tokens[i] = nltk.word_tokenize(file_content[i])
	obj.addDocument(titles[i],tokens[i])
print obj.similarities (q_tok)

