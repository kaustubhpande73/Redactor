# cs5293sp22-project1
Kaustubh Pande 

Project Objectives: In this project, we designed a system that accepts plain text documents then detect and redact “sensitive” items. As part of this project, we were asked to redact names, addresses, genders,dates ,phonenumbers and concepts.



Setup.py: The setup.py file contains the details about the project - name, author, version,... from setuptools import setup, find_packages

setup( name='project1', version='1.0', author='Kaustubh Pande', authot_email='kaustubhpande@ou.edu', packages=find_packages(exclude=('tests','docs')) setup_requires=['pytest-runner'], tests_require=['pytest'] )

setup.cfg: contains - [aliases] test=pytest

[tool:pytest] norecursedirs = .*, CVS, _darcs, {arch}, *.egg, venv

The Project functions are-
Names - to redact names I have used nltk library to identify entities which are "PERSON" and redacted these entities and replaces them with \u2588 character. 
    
    def Names(data):
    text = data
    doc=nlp(text)
    text = re.sub('\n',' ',text)
    text = re.sub('\t',' ',text)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        if ent.label_=='PERSON':
            text=text.replace(ent.text,'\u2588'*len(ent.text))
    return text

Testing it with sample data  = "David Fincher should release the season 3 on Mindhunter"

The output recieved = █████████████ should release the season 3 of ██████████

Phone - This funtion redacts the phone number for the document. I have used regular expression to identify the phone numbers from the text and replace them with them with \u2588 character. It redacts numbers in the format ###-###-####.
    
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
Testing it with sample data = "my phone is 233-245-2211" 
The output recieved = my phone is ████████████

E-mail - This was not mentioned in the project requirements, but I have added it. It accepts regular expression for email id and replaces it with \u2588 character.
    
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
Testing with sample data = "release Mindhunter david.fincher@netflix.com" 
The output recieved = release Mindhunter █████████████████████████

Date - For this function, I have used the nltk library to identify the DATA entity and replace it with \u2588 character. I tried using regular expression, but it was not capturing satisfyingly. This should capture most of the dates.
    
    def date(data):
    text = data
    doc=nlp(text)
    text = re.sub('\n',' ',text)
    text = re.sub('\t',' ',text)
<!-- #    """I tried using regex, but it won't capture the right dates, so used entity label to capture dates.
 #      It is not perfect but captures most dates"""
#     regex_date = '(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d'
#     date = re.findall(regex_date,text)
#     for i in text:
#         for j in date:
#             j=j.replace(i,'\u2588'*len(i)) -->
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        if ent.label_=='DATE':
            text=text.replace(ent.text,'\u2588'*len(ent.text))

Testing with sample data = "my birthday is in 19 Nov 1996" 
Output recieved = my birthday is in ███████████

Gender - For this function, I have made use of regular expressions. It does not give accurate redactions. But works on a few workcases.

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


Address - For this I have used regular expression to identify the addresses and replace them with \u2588 character. Again this is not accurate. Should work most of the time. I tried using the entity "FAC", but it was not giving me a satisfied output too.

     def address(data):
    text = data
    doc=nlp(text)
    text = re.sub('\n',' ',text)
    text = re.sub('\t',' ',text)
    regex_gender = r'^(\d+) ?([A-Za-z](?= ))? (.*?) ([^ ]+?) ?((?<= )APT)? ?((?<= )\d*)?$'
    gender = re.findall(regex_gender,text)
    for i in gender:
        text = text.replace(i,'\u2588'*len(i))
    

<!-- # for ent in doc.ents:
#         #print(ent.text, ent.start_char, ent.end_char, ent.label_)
#         if ent.label_=='FAC':
#             text=text.replace(ent.text,'\u2588'*len(ent.text))

 -->
Concept - This function,  takes one word or phrase that represents a concept and identifies it within the text.
      
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
   

###Important Bugs and run and assumptions:
1. The phone number format I used is ###-###-####. 
2. The address function may not give accurate results. I used two approaches, but have gone with regex approach rather than entity approach.
3. For output, I have used mainly Jupyter Notebooks to verify my results. 
4. I have added the sample file of which I run the code - "sample.txt"
5. I was unable to used glob and emplement the stat function
6. My main file has bugs. Running all function tests would give a preferred output.



Links for references used :
1. https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7das

2. Date - https://www.youtube.com/watch?v=o8Je7hPgsdU

3. To download stop words - nltk.download('stopwords')
4. Email - https://www.tutorialspoint.com/python_text_processing/python_extract_emails_from_text.html

5. https://www.codegrepper.com/code-examples/python/phone+number+regex+python
