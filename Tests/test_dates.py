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

data = "my birthday is on 19 Nov 1996" 

def date(data):
    text = data
    doc=nlp(text)
    text = re.sub('\n',' ',text)
    text = re.sub('\t',' ',text)
    """I tried using regex, but it won't capture the right dates, so used entity label to capture dates.
       It is not perfect but captures most dates"""
#     regex_date = '(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d'
#     date = re.findall(regex_date,text)
#     for i in text:
#         for j in date:
#             j=j.replace(i,'\u2588'*len(i))
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        if ent.label_=='DATE':
            #stats.append([entity.text,len(entity.text),'Date'])
            text=text.replace(ent.text,'\u2588'*len(ent.text))
    return text
        
