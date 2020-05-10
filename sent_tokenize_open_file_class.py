# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:00:35 2020

@author: Ola
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from pathlib import Path
from nltk.stem import WordNetLemmatizer
import os
class TextProcessor:
    
    def readFile(self, path):
        text=''
        with open(path,'r')as f:
            text = f.read()
        return text
    
    def sentTokenize(self, text):
        text = self.readFile(text)
        sentences = sent_tokenize(text)
        return sentences
    
    def wordTokenize(self, text):
        text = self.readFile(text)
        words = word_tokenize(text)
        return words
#lemmatizer = WordNetLemmatizer()
#words_lemmetized = [lemmatizer.lemmatize(word) for word in words]
    def lemmatizeTokenize(self, text):
        text = self.readFile(text)
        words = word_tokenize(text)
        lemmatizer = WordNetLemmatizer()
        words_lemmatized = [lemmatizer.lemmatize(word) for word in words]
        return words_lemmatized
    
#pos = nltk.pos_tag(words)
#dicts.append({"TITLE":"POS","CONTENT":pos})    
    def posTagging(self, text):
        text = self.readFile(text)
        words = word_tokenize(text)
        pos = nltk.pos_tag(words)
        return pos
    
    def dicts(self,path):
        text_list = []
        text = self.readFile(os.path.join(path))
        text_list.append({'title':path,'content':text})
        sentences = self.sentTokenize(os.path.join(path))
        text_list.append({'title':'sent tokenize','content':sentences})
        words = self.wordTokenize(os.path.join(path))
        text_list.append({'title':'word tokenize','content':words})
        lemmatize = self.lemmatizeTokenize(os.path.join(path))
        text_list.append({'title':'lemmatize tokenize','content':lemmatize})
        
        posTagging = self.posTagging(os.path.join(path))
        text_list.append({'title':'posTagging','content':posTagging})
        return text_list
molo = TextProcessor()

list_of_files = molo.dicts('plik.txt')
for item in list_of_files:
    print(item)
    print()