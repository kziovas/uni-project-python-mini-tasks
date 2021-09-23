# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:37:27 2019

@author: Kostas Ziovas
"""

#text='This is a test text \t to see if i can remove all \n spaces'

def remove_space(filename):
    f=open(filename,'r')
    text=f.read()
    print("Original text:\n",text)
    new=text.replace(' ','')
    new=new.replace('\t','')
    new=new.replace('\n','')
    f.close()
    f=open('new.txt','w+')
    f.write(new)
    f.close()
    print("\nNew text:\n",new)
    return (new)
    
    
remove_space('testfile.txt')
