



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
