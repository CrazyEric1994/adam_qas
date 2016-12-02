import time
import spacy.vocab


def get_wh_word(sent):

    for token in sent:
        print(token.tag_)
        if token.tag_ == "WRB" or token.tag_ == "WDT" or token.tag_ == "WRB":
            return token.text
    return "rest"

question = "What year did the Titanic sink ?"

start_time = time.time()

en_nlp = spacy.load('en')
en_doc = en_nlp(u'' + question)

for sent in en_doc.sents:

    head_word = get_wh_word(sent)
    print(head_word)