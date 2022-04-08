







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
