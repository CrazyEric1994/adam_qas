import spacy
import time
from nltk import Tree


def get_pos_tags(sent):
    pos_tagset = []
    for token in sent:
        # pos_tagset[token.text] = token.pos_                   # Coarse Grained POS
        pos_tagset.append(token.text + "/" + token.tag_)        # Fine Grained POS
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


input_question = "How can there be any sin in sincere? Where is the good in goodbye Mr. Obama?"

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

    # to_nltk_tree_dep(sent.root).pretty_print()            # To print the Dependency Tree


end_time = time.time()
print("Time: ", end_time - start_time)
