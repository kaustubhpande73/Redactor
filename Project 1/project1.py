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
raw_file = open('sample.txt')
data = raw_file.read()

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
def address(data):
    text = data
    doc=nlp(text)
    text = re.sub('\n',' ',text)
    text = re.sub('\t',' ',text)
    regex_gender = r'^(\d+) ?([A-Za-z](?= ))? (.*?) ([^ ]+?) ?((?<= )APT)? ?((?<= )\d*)?$'
    gender = re.findall(regex_gender,text)
    for i in gender:
        text = text.replace(i,'\u2588'*len(i))
    

# for ent in doc.ents:
#         #print(ent.text, ent.start_char, ent.end_char, ent.label_)
#         if ent.label_=='FAC':
#             #stats.append([entity.text,len(entity.text),'Date'])
#             text=text.replace(ent.text,'\u2588'*len(ent.text

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
