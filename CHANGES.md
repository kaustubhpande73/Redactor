* Missing/No Features Found- Names - I tested this function, it was working. I have added it to the code for calling rather than the main function. It works.
* Missing/No Features Found - Gender
* Missing/No Features Found- Phone Number - I have modified the regex to match phone numbers. The format it matches is ###-###-####.
* Missing/No Features  Found- Concept - I have modified this function by using lemmatization and tokenizing the words for concepts. It accepts the data(input) and the keyword for concept.
* Missing/No Features Found - Dates - I have replaced the use of regex for this and instead used DATE entity to match dates using nlp.
* Missing/No Features - Addresses - Again for this, I have removed the regex approach and used the 'FAC' entity instead to catch the addresses.
* Missing Stats - I could not add the stat function first time. This time I have stored them as a dataframe, where it first redacted words, length and type.
* File names not re-assigned correctly - For this I have renamed the redacted text with .redacted extension.
* Output files not stored in respective folder - I have added it to the code. It should create .redacted and stats.txt files.
