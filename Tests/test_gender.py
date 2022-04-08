import project1
import pytest
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import spacy
from spacy import displacy
import pandas as pd
from nltk.corpus import wordnet
import sys
nlp=spacy.blank("en")
nlp =spacy.load("en_core_web_sm")


def gender(data):
    text = data
    doc=nlp(text)
    text = re.sub('\n',' ',text)
    text = re.sub('\t',' ',text)
    regex_gender = r' he | He | him | Him | She | she | her | Her | Man | man | Woman | woman | Men | men | Women | women '
    gender = re.findall(regex_gender,text)
    for i in gender:
        text = text.replace(i,'\u2588'*len(i))
    return text
    assert text != None    
