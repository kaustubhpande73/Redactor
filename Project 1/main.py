import project1
import sys


  raw_file = open('sample.txt')
  data = raw_file.read()
  list=[]
  list=sys.argv
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
            data=concepts(data,list[i+1])
