"""

    You Might need to download some packages to run this code
    You'll get those names when you run the code [marked in red color]
    just type the following code in the terminal:
    
    > python3
    [Then python shell will start, just type the follwing lines there]
    
    >>> import nltk
    >>> nltk.download('averaged_perceptron_tagger')
    >>> nltk.download('punkt')
    >>> nltk.download('stopwords')
    
"""


import csv
from curses.ascii import ispunct
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))


# Required Variables
tagged_words_lists = []
all_nouns = dict(set())
all_verbs = dict(set())
set_of_nouns = set()
set_of_verbs = set()


# Read the input text
txt = ""
with open('input.txt', 'r') as f:
    txt = f.read()
f.close()


# Tokenize the text
tokenized = sent_tokenize(txt)


# Word tokenizers is used to find the words and punctation
for i in tokenized:

    # Word tokenizers is used to find the words
    # and punctuation in a string
    wordsList = nltk.word_tokenize(i)

    # removing stop words from wordList
    wordsList = [w for w in wordsList if not w in stop_words]

    # Using a Tagger. Which is part-of-speech
    # tagger or POS-tagger.
    tagged = nltk.pos_tag(wordsList)

    # Appending the tagged words to the list
    tagged_words_lists.append(tagged)


# Make a set of all the nouns and verbs
for i in tagged_words_lists:
    
    for t in i:
        pos = t[1]
        word = t[0].strip()
        
        if  len(word) == 1 and ispunct(word):
            continue
        
        if pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS':
            all_nouns[word] = pos
            set_of_nouns.add(word.lower())
            
        elif t[1] == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ':
            all_verbs[word] = pos
            set_of_verbs.add(word.lower())


# Function to extract words from the set
def extract_words(fileName, heading, tagger_set):
    with open(fileName,"w+") as fff:
        writer = csv.writer(fff)
        writer.writerow(heading)

        id = 1
        f = open(fileName, 'w+')
        for i in tagger_set:
            x = i.title()
            if len(x) == 1:
                if ispunct(ord(x)) == True:
                    f.write(str(id) + x + "\n")
                    writer.writerow([id,x])
                    id += 1
            else:
                f.write(str(id) + x + "\n")
                writer.writerow([id,x])
                id += 1
        

        f.close()
    fff.close()


# extract Nouns
extract_words('Nouns.csv', ['Serial No.', 'Noun'], set_of_nouns)


# extract Nouns
extract_words('Verbs.csv', ['Serial No.', 'Verb'], set_of_verbs)