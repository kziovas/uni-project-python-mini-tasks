# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:02:31 2019

@author: Kostas Ziovas
"""

#-----Library calls----#
from string import ascii_lowercase
import numpy as np
import operator as op

#-----------Definitions----------#
name="ex11.txt"


#----------Function Definitions--------------#

#Function that calculates the statistics for each letter
def lett_stat(name):
    f=open(name,'r')
    text=f.read()
    text=text.lower()
    letnum=[0]*26
    count=0
    for c in ascii_lowercase:   
        letnum[count]=text.count(c)
        count+=1
               
    letsum=sum(letnum)   
    letstat=np.divide(letnum,letsum)
    letstat=np.multiply(letstat,100)
    
    finalstat = []
    count=0
    for c in ascii_lowercase:   
        finalstat.append([letnum[count],letstat[count],c])
        count+=1

    finalstat=sorted(finalstat,key=op.itemgetter(0))
    return(finalstat)

#Function that displays the results of the statistical analysis in a nice way
def print_stat(stat):
    print("----------Letter Statistics of a Text----------------")
    print("The frequency of the letters appearance in ascending order: ")
    for i in range(len(stat)):
        print(stat[i][2]," : ","%.2f" %stat[i][1],"%", " count: ",stat[i][0])

#-------------------------------------------------------------------------#
#---------------------Main Program----------------------------------------#
print("The file to be analyzed is ex11.txt")
stat=lett_stat(name)
print_stat(stat)      