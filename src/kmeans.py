import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from collections import Counter


def get_tokens(file_path):
    with open(file_path, 'r') as text_file:
        text = text_file.read()
        lowers = text.lower()
        tokens = nltk.word_tokenize(lowers)
        tokens = [''.join(c for c in s if c not in string.punctuation) for s in tokens]
        tokens = [s for s in tokens if s]
        return tokens


def remove_stop():
    tokens = get_tokens(path)
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    return filtered


def stemming_text():
    stemmer = SnowballStemmer("english")
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

print("----------------------------------------Stage 1 After Tokenising----------------------------------------------")
path = '/home/amit/IdeaProjects/adam_qas/corpora/barack.txt'
tokens = get_tokens(path)
count = Counter(tokens)
print(tokens)
print("----------------------------------------Stage 2 After Removing Stopwords---------------------------------------")
print(remove_stop())
print("----------------------------------------Stage 3 After Stemming Algorithms--------------------------------------")
print(stemming_text())
print()