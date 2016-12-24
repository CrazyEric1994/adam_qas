import spacy
import time
from nltk import Tree
from spacy.symbols import nsubj, nsubjpass, csubj, csubjpass, agent, expl
from spacy.symbols import dobj, attr, iobj, oprd
from spacy.symbols import pobj, pcomp
from spacy.symbols import amod, det
from spacy.symbols import NOUN, PROPN, PRON


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


def get_named_entity(sent):
    entity_set = []
    for token in sent:
        if token.ent_type != 0:
            entity_set.append(token.text + "/" + token.ent_type_)
    return entity_set


def get_dependency(sent):
    dependency_set = []
    for token in sent:
        dependency_set.append(token.text + "/" + token.dep_)
    return dependency_set


def tok_format_dep(tok):
    return "_".join([tok.orth_, tok.dep_])


def to_nltk_tree_dep(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(tok_format_dep(node), [to_nltk_tree_dep(child) for child in node.children])
    else:
        return tok_format_dep(node)


# input_question = "How can there be any sin in sincere? Where is the good in goodbye?"
# input_question = "What is the full form of .com?"
input_question = "Which country has Hindi as an official language other than India?"

start_time = time.time()

en_nlp = spacy.load('en')
en_doc = en_nlp(u'' + input_question)

for sent in en_doc.sents:
    pos_tagset = get_pos_tags(sent)
    print(pos_tagset)

    lemma_set = get_lemma_set(sent)
    print(lemma_set)

    entity_set = get_named_entity(sent)
    print(entity_set)

    dependency_set = get_dependency(sent)
    print(dependency_set)

    to_nltk_tree_dep(sent.root).pretty_print()  # To print the Dependency Tree

question_frame = ""

for sent in en_doc.sents:
    for token in sent:
        if (token.dep == nsubj or token.dep == csubj or token.dep == nsubjpass or token.dep == csubjpass) and (
                token.pos == NOUN or token.pos == PROPN):
            """print(token.head, ">", token.text)
            print(list(token.children))
            print(list(token.conjuncts))
            print(list(token.subtree))
            print(list(token.ancestors))"""
            for children in token.children:
                if children.dep == det and token.i > children.i:
                    print(children.text, token.text)
                    question_frame = "[ " + children.text + " " + token.text + " [ "
                elif children.dep == det and token.i < children.i:
                    print(token.text, children.text)
                    question_frame = "[ " + token.text + " " + children.text + " [ "
                else:
                    print(token.text)
                    question_frame = "[ " + token.text + " [ "
                print("[" + token.text + " : ")

        """if (token.dep == attr or token.dep == dobj or token.dep == iobj or token.dep == oprd) and (token.pos == NOUN or token.pos == PRON or token.pos == PROPN):
            print("\t" + token.text)"""
    print(question_frame)

end_time = time.time()
print("Time: ", end_time - start_time)
