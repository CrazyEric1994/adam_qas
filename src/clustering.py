#-----------------------Imports---------------------------------
import numpy as np
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import sys
import wikipedia
potus = wikipedia.page("donald trump")
obj = potus.content

def create():
    print("creating new  file")
    name=input ("enter the name of file:")
    try:
        name=name+"."+"txt"
        file=open(name,'a')
        file.write(obj)
        file.close()
    except:
        print("error occured")
        sys.exit(0)

create()