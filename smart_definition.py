# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 12:28:00 2016

@author: Max
"""

#clever definition finder

from nltk.corpus import wordnet as wn
from nltk.tag import pos_tag



def smart_definition(sentence):
    sentence=sentence.replace("?","")
    tagged_sent=pos_tag(sentence.split())
    print(tagged_sent)
    for word in tagged_sent:
        if word[1]=='NN':
            noun=word[0]
            break            
    noun=str(noun)
    for i in range(1,5):
        iteration=str(i)
        string_test=noun+'.n.0'+iteration
        descript=wn.synset(noun+'.n.0'+iteration).definition()
        descripted=descript.split()
        tagged_sent_2=pos_tag(descripted)
        #print(tagged_sent_2)
        subj_list=[]
        for item in tagged_sent_2:
            #print(item[0])
            new_word=str(item[0])
            new_word=new_word.replace("\\","")
            new_word=new_word.replace(":","")
            #print(new_word)
            if item[1]=='NN' and new_word.isalnum()==True:
                subj_list.append(new_word)
            elif item[1]=='NNS' and new_word.isalnum()==True:
                string=str(wn.synsets(new_word)[0])
                #print(string)
                string=string[8:]
                string=string[:-7]
                #print(string)
                subj_list.append(string)
        #print(subj_list)
        comp_list=[]
        original_def=wn.synset(noun+'.n.0'+iteration)
        iteration_2=0
        for item_2 in subj_list:
            iteration_2+=1
            item_2=item_2.replace(":","")
            #print(item_2)
            new_def=wn.synset(item_2+'.n.01')
            comp_list.append(new_def.path_similarity(original_def))
        max_index=comp_list.index(max(comp_list))
        key_word=subj_list[max_index]
        response=input('Do you mean the '+str(key_word)+'? ')
        if response.lower()=='yes':
            print('Excellent! Glad to help. Here is the definition: "'+str(descript)+'"')
            break

        
smart_definition('What is a mouse?')
    
    