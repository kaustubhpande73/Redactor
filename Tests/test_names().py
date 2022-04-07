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

data = "David Fincher should release the season 3 of Mindhunter" 

def Names(data):
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(data)
# for ent in doc.ents:
#     if ent.label_ == "PROPN":
#displacy.render(doc, style='ent') #visualization for entity names using displacy
# name = []
# ent for ent in doc.ents if ent.label == spacy.symbols.PERSON:
    text = data
    doc=nlp(text)
    text = re.sub('\n',' ',text)
    text = re.sub('\t',' ',text)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        if ent.label_=='PERSON':
            stats.append([entity.text,len(entity.text),'Name'])
            text=text.replace(ent.text,'\u2588'*len(ent.text))
    return text
    assert text != None
