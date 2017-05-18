# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import nltk

#nltk.download('all')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


example_test2 = "One of the largest elements to any data analysis, natural language"
example_test = "One of the largest elements to any data analysis, natural language processing included, is pre-processing. This is the methodology used to clean up and prepare your data for analysis. "

#with open('exemplo_teste.txt','r') as f:
#    for line in f:
#       example_test = line

#train_text = state_union.raw(example_test)
#sample_text = state_union.raw("exemplo_teste.txt")


stop_words = set(stopwords.words("english"))
words = word_tokenize(example_test)
filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

custom_sent_tokenizer = PunktSentenceTokenizer(example_test2)
tokenized = custom_sent_tokenizer.tokenize(example_test)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            # Named Entity Recognition
            namedEnt = nltk.ne_chunk(tagged)
            namedEnt.draw()
            
            # Faz o "chunking das palavras"
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged, binary=True)
            
            print(chunked)
    
    except Exception as e:
        print(str(e))

process_content()

# lematizacao
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
for w in filtered_sentence:
   print(ps.stem(w))
   print(lemmatizer.lemmatize(w))

        
