import re
import string

import nltk
from nltk import PorterStemmer
from nltk import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from collections import Counter
def porter_stemmer(text):
    stem = PorterStemmer()
    lst = []
    for token in nltk.word_tokenize(text):
        lst.append(stem.stem(token))

    return " ".join(lst)


def lancaster_stemmer(text):
    stem = LancasterStemmer()
    lst = []
    for token in nltk.word_tokenize(text):
        lst.append(stem.stem(token))

    return " ".join(lst)


def word_net_lemmatizer(text):
    lem = WordNetLemmatizer()
    lst = []
    for token in nltk.word_tokenize(text):
        lst.append(lem.lemmatize(token))

    return " ".join(lst)

def create_gram(text, n):
    txt = " ".join(text)
    tokens = txt.split()
    gram = [" ".join(tokens[i:i+n]) for i in range (len(tokens)-n+1)]
    print("\n Result_Create Gram \n")
    print(gram)
    return gram

def counter_gram(text,n):
    tokens =create_gram(text, n)
    print("\n Result_Count Grams \n")
    return Counter(tokens)