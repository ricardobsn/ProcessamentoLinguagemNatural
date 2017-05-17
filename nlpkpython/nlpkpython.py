# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import nltk

#nltk.download('all')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
f = open('exemplo_teste.txt', 'r')
#example_test = f.read()
example_test = "One of the largest elements to any data analysis, natural language processing included, is pre-processing. This is the methodology used to clean up and prepare your data for analysis. "

#print(sent_tokenize(example_test))
#print(word_tokenize(example_test))

stop_words = set(stopwords.words("english"))
words = word_tokenize(example_test)
filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
        
 # print(filtered_sentence)

ps = PorterStemmer()
for w in filtered_sentence:
    print(ps.stem(w))

    