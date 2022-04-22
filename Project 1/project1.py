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
list=[]
list=sys.argv
stats=[[]]
#     for i in files:
#     File = open(i) 
#     data = File.read()
            
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
#         print(ent.text, ent.start_char, ent.end_char, ent.label_)
        if ent.label_=='PERSON':
            text=text.replace(ent.text,'\u2588'*len(ent.text))
            stats.append([ent.text,len(ent.text),'Name'])

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
        stats.append([j,len(j),'Phone'])

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
    
    # data = "The year is 2002"
    text = data
    doc=nlp(text)
    text = re.sub('\n',' ',text)
    text = re.sub('\t',' ',text)
#     """I tried using regex, but it won't capture the right dates, so used entity label to capture dates.
#        It is not perfect but captures most dates"""
#     regex_date = '(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d'
#     date = re.findall(regex_date,text)
#     for i in text:
#         for j in date:
#             j=j.replace(i,'\u2588'*len(i))
    for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)
        if ent.label_=='DATE':
         stats.append([ent.text,len(ent.text),'Date'])
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
    for ent in doc.ents:
                #print(ent.text, ent.start_char, ent.end_char, ent.label_)
            if ent.label_=='FAC':
                text=text.replace(ent.text,'\u2588'*len(ent.text))
                stats.append([ent.text,len(ent.text),'Date'])
    return text
    
def concept(data, concept):
    concept_list = []
    concept_count = 0
    synonyms = wordnet.synsets(concept)
    for i in synonyms:
        temp = i.lemma_names()
        for f in temp:
            if f not in concept_list:
                concept_list.append(f)
 
    for k in nltk.sent_tokenize(data):
        for l in concept_list:
            if l.lower() in k.lower():
                data = data.replace(k, len(k)*'\u2588')
                stats.append([k,len(k),'Concept'])
#                 concept_count += 1
    return data, concept_list


nlp=spacy.blank("en")
nlp =spacy.load("en_core_web_sm")
raw_file = open('sample.txt')
data = raw_file.read()
list=[]
list=sys.argv
stats=[[]]
#     for i in files:
#     File = open(i) 
#     data = File.read()
for i in range(len(list)):
    if (list[i] == '--names'):
        data=Names(data)
    elif (list[i] == '--phones'):
        data=email(data)
    elif (list[i] == '--email'):
        data=email(data)
    elif (list[i] == '--date'):
        data=date(data)
    elif (list[i] == '--phones'):
        data=gender(data)
    elif (list[i] == '--concept'):
        data=concept(data,list[i+1])
    elif list[i] == '--output':
            file=open(i[:-4]+'.redacted',"w+")
            file.write(data)
            file.close()
    elif list[i] == '--stats':
            df=pd.DataFrame(stats)
            df.to_csv(r'stats.txt',header=None, index=True, sep=' ')
