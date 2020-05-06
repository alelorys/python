# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:21:21 2020

@author: Ola
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
text = """Look at the time.
It’s nine o’clock and you have to go.
I want you to stay.
But it’s getting late, we both heard mommy say.
Boy, you’d better go now.
Time is running, seven’s coming.
Don’t put up a fight.
Time is up for tonight.

We’re together lost forever.
Time is here and love is easy.
We’re forever paired together.
Shine wherever we go.
We’re together lost forever.
Time and say we love it see say.
We’re forever part together.
Shine wherever we go.
Let the flower of your soul.
Fly around the love we’ll grow tonight.

Later I lied.
I’m in my bed and I miss you so.
Feeling the same.
Are you also feeling lost inside this game?
You make me fly high.
Getting lazy, going crazy.
All I wanna do is to.
Hold you in my arms.

We’re together lost forever.
Time is here and love is easy.
We’re forever paired together.
Shine wherever we go.
We’re together lost forever.
Time is here and love is easy.

We’re forever paired together.
Shine wherever we go.
Let the flower of your soul.
Fly around the love we’ll grow tonight.

You make me fly high.
Getting lazy, going crazy.
All I wanna do is to.
Hold you in my arms.

We’re together lost forever.
Time is here and love is easy.
We’re forever paired together.
Shine wherever we go.
We’re together lost forever.
Time is here and love is easy.
We’re forever paired together.
Shine wherever we go.
Let the flower of your soul.
Fly around the love we’ll grow tonight."""
song = []
song.append({"TITLE":"Forever","CONTENT":text})
sentences = sent_tokenize(text)
song.append({"TITLE":"Sent tokenize","CONTENT":sentences})

words = word_tokenize(text)
song.append({"TITLE":"word tokenize","CONTENT":words})

lemmatizer = WordNetLemmatizer()
words_lemmetized = [lemmatizer.lemmatize(word) for word in words]

song.append({"TITLE":"Lemmatize","CONTENT":words_lemmetized})

pos = nltk.pos_tag(words)
song.append({"TITLE":"POS","CONTENT":pos})
print(song)