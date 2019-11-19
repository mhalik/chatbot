# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:23:02 2016

@author: Max
"""



def greeting(prompt):
    with open("ai_memory.txt", "r") as f:
        for line in f:
            words=line.split()
            things=prompt.split( )
            for thing in things:
                if thing.lower() in words:
                    print("I know that word!")
                    break
                else:
                    new_word=input("Could you type the word that you used as a greeting? If you didn't type a greeting, could you please write 'n/a'? ")
                    if new_word=='n/a':
                        break
                    f.close()
                    with open("ai_memory.txt", "a") as myfile:
                        myfile.write(" "+str(new_word.lower()))
                    myfile.close()
                    break
                break
            break

                            
