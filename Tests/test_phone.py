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

data = "my phone is 233-245-2211"

def phone(data):
    text = data
    doc=nlp(text)
    text = re.sub('\n',' ',text)
    text = re.sub('\t',' ',text)
    regex_phone=r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]?\d{4}|\d{3}[-\.\s]??\d{4}' # format - ###-###-####
    phone=re.findall(regex_phone, text)
    for j in phone:
        text=text.replace(j,'\u2588'*len(j))
    return text
    assert text != None
