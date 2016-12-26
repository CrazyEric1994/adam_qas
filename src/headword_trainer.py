import os
import spacy
from spacy.symbols import nsubj,attr,NOUN,PROPN,PRON

path = os.path.dirname(os.path.realpath(__file__))
path = path.replace("/src", "/corpora/")
fp = open(path+"train_5500.label.txt", "r")
fp_train = open(path+"train_5500_headword.txt", "w")

en_nlp = spacy.load('en')


"""

WH Type
Root > POS


"""

for record in fp:
    training_data = record.split(" ", 1)
    if training_data[1].startswith("What"):
        head_word = "null"
        question = training_data[1].replace("\n", "")
        en_doc = en_nlp(u'' + question)
        for sent in en_doc.sents:
            for token in sent:
                if token.dep == nsubj and (token.pos == NOUN or token.pos == PROPN):
                    head_word = token.text
                elif token.dep == attr and (token.pos == NOUN or token.pos == PROPN):
                    head_word = token.text

        fp_train.write(training_data[0]+" "+question+" ("+head_word+")\n")
fp_train.close()
