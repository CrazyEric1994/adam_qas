import spacy
import time


def get_pos_tags(sent):
    pos_tagset = []
    for token in sent:
        # pos_tagset[token.text] = token.pos_                   # Coarse Grained POS
        pos_tagset.append(token.text + "/" + token.tag_)  # Fine Grained POS
    return pos_tagset


def get_lemma_set(sent):
    lemma_set = []
    for token in sent:
        lemma_set.append(token.text + "/" + token.lemma_)
    return lemma_set


input_question = "How can there be any sin in sincere? Where is the good in goodbye?"

start_time = time.time()

en_nlp = spacy.load('en')
en_doc = en_nlp(u'' + input_question)

for sent in en_doc.sents:
    pos_tagset = get_pos_tags(sent)
    lemma_set = get_lemma_set(sent)
    print(pos_tagset)
    print(lemma_set)

end_time = time.time()
print("Time: ", end_time - start_time)
