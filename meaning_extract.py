# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 16:06:35 2017

@author: Max
"""

from nltk.corpus import wordnet as wn
from nltk.tag import pos_tag
import re

def meaning_extract(sentence):
    sentence=sentence.replace('?','')
    sentence=sentence.replace('.','')
    sentence=sentence.replace(',','')
    sentence=sentence.replace(';','')
    sentence=sentence.replace('-','')
    print(sentence)
    tagged_sent=pos_tag(sentence.split())
    print(tagged_sent)
    
#vbg=verb gerund
#vb