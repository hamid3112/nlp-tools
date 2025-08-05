#!/usr/bin/env python
# coding: utf-8

# In[15]:


import nltk
import re 
import string
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag

# دانلود منابع مورد نیاز
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")

punctuation = string.punctuation.replace("'", "")
stop_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def preprocessing_text(text):
    try:
        # lowercase
        text = text.lower()
        # remove punctuation
        text = re.sub(rf"[{re.escape(punctuation)}]", " ", text)
        # remove extra whitespace
        text = " ".join(text.split())
        # tokenize
        tokens = word_tokenize(text)
        # remove stopwords
        tokens = [word for word in tokens if word not in stop_words]
        # lemmatize
        tag = pos_tag(tokens)
        lemma = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in tag]
        return lemma
    except Exception as error:
        print(f"Error is: {error}")
        return []

