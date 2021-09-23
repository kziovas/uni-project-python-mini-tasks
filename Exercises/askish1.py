# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:56:48 2019

@author: Kostas Ziovas
"""


#----------Definitions---------#
list=[[2,5],[7,11],[0,56],[1,8],[38,41]]
#print(list[2][1])



#-----------Function Definitions--------------#
def maxminIntervals(list):
    x=len(list)
    vmax=list[0][1]-list[0][0]
    vmin=list[0][1]-list[0][0]
    maxlst=[list[0]]
    minlst=[list[0]]
    for i in range(x):
        dif=list[i][1]-list[i][0]
        
        if (dif > vmax):
            vmax=dif
            maxlst[0]=list[i]
            
          
        if (dif < vmin):
            vmin=dif
            minlst[0]=list[i]
    
    for i in range(x):
        dif=list[i][1]-list[i][0]
        if(dif==vmax and maxlst[0]!=list[i]):
            maxlst.append(list[i])
        if(dif==vmin and minlst[0]!=list[i]):
            minlst.append(list[i])
    print("max=",maxlst," ","min=",minlst)
    return maxlst,minlst

#-------------------------------------------------------------------------#
#---------------------Main Program----------------------------------------#    
maxminIntervals(list)