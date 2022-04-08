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



def concepts(text,concept):

    sent = nltk.tokenize.line_tokenize(text)

    sen_list,mean,words= [],[],[]

    synaset = wordnet.synsets(concept)

    for i in range(len(synaset)):

        mean.append(synaset[i].lemmas()[0].name())

   

    for line in range(len(sent)):

        words = nltk.tokenize.word_tokenize(sent[line])

        flag = 0

        for j in range(len(words)):

            for i in range(len(mean)):

                if (mean[i] == words[j] and flag == 0):

                    flag = flag + 1

                    sen_list.append(sent[line])

    return sen_list
