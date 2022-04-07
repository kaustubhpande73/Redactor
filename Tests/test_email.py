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

data = "release Mindhunter david.fincher@netflix.com"



def email(data):
  text = data
  doc=nlp(text)
  text = re.sub('\n',' ',text)
  text = re.sub('\t',' ',text)
  regex_email = '[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+'
  email = re.findall(regex_email,text)
  for i in email:
      text = text.replace(i,'\u2588'*len(i))
  return text
