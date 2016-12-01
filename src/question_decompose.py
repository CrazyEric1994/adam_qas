import spacy

class QuestionDecompose:

    """ Lower Case, Sentence Segmentation, Spell Check and other Pre-processing and Decomposition """

    def __init__(self, question):
        self.question = question
        self.en_nlp = spacy.load('en')
        self.en_doc = self.en_nlp(u''+question)

    def to_lowercase(self):
        return self.question.lower()

    def segment_sentence(self):
        sentences = self.en_doc.sents
        return list(sentences)
