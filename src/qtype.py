import time
import re
import spacy.vocab


def get_wh_word(sent):
    for token in sent:
        print(token.tag_)
        if token.tag_ == "WRB" or token.tag_ == "WDT" or token.tag_ == "WRB":
            return token.text
    return "rest"


def get_head_word(sent, wh_word):

    wh_word = wh_word.lower()
    re.search('(\bwhat)+\s((is)|(are))+\s((a)|(an)|(the))')

    if wh_word == "when" or wh_word == "where" or wh_word == "why":
        return ""                                                               # informative enough
    elif wh_word == "how":
        return ""                                                               # return word following how
    elif wh_word == "what":
        return ""                                                               # match all pattern rules except for HUM:desc
    elif wh_word == "who":
        return "HUM:desc"
    else:
        return ""


question = "What year did the Titanic sink ?"

start_time = time.time()

en_nlp = spacy.load('en')
en_doc = en_nlp(u'' + question)

for sent in en_doc.sents:
    wh_word = get_wh_word(sent)
    print(wh_word)

    head_word = get_head_word(sent, wh_word)
    print(head_word)


end_time = time.time()
print("Time: ", end_time - start_time)