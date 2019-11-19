# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 17:32:22 2017

@author: Max
"""

from nltk.corpus import wordnet as wn
from nltk.tag import pos_tag
from nltk.corpus import gutenberg
import random as r


bible_sents=gutenberg.sents('bible-kjv.txt')
bible_sents=bible_sents[15943:16779]

def proverbs(sentence):
    sentence=sentence.replace("?","")
    sentence=sentence.replace(".","")
    tagged_sent=pos_tag(sentence.split())
    #print(tagged_sent)
    try:
        for word in tagged_sent:
            if word[1]=='NN':
                noun=word[0].lower()
                break
            elif word[1]=='NNS':
                noun=word[0].lower()
                break
            elif word[1]=='JJ':
                noun=word[0].lower()
                break
        index_list=[]
        i=0
        for sent in bible_sents:
            for word in sent:
                if noun==word.lower():
                    index_list.append(i)
            i+=1
        try:
            choice=r.choice(index_list)
            proverb=bible_sents[choice]
            link=' '
            proverb=link.join(proverb)
            print(proverb)
        except IndexError:
            print('I cannot find wisdom on that subject. Try another.')
    except UnboundLocalError:
        print('I do not understand the subject you are searching. Try a synonym?')

                
                