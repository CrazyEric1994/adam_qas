import nltk
from nltk.tokenize import TweetTokenizer
from nltk.stem.snowball import SnowballStemmer

tknzr = TweetTokenizer()
t1 = open ("/home/amit/IdeaProjects/adam_qas/corpora/barack.txt",'rw').read()
s0 = t1
st = []
st = tknzr.tokenize(s0)
for item in st:
    t1.write("%s",item)



