# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 13:46:38 2016

@author: Max
"""

from nltk.corpus import wordnet as wn
dog = wn.synset('dog.n.01')
cat = wn.synset('cat.n.01')
fish = wn.synset('fish.n.01')
print(dog.path_similarity(cat))
print(fish.path_similarity(dog))
print(dog.path_similarity(dog))

print(wn.synset('dog.n.01').definition())

def definition_please(word):
    total_string=word+'.n.01'
    result=wn.synset(total_string).definition()
    print(result)