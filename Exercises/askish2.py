# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:34:44 2019

@author: Kostas Ziovas
"""





#----------Function Definitions--------------#
def single_dig(number):
    sum1=0
    leng=len(number)
    for i in range(leng):
        num=int(number[i])
        sum1=sum1+num
    strsum=str(sum1)
    if(len(strsum)<=1):
        return (strsum)
    else:
       return single_dig(strsum)
 
#-------------------------------------------------------------------------#
#---------------------Main Program----------------------------------------#    
number=input("Dwse ena akeraio arithmo: ")    
res=single_dig(number)
print("To arthroisma twn psifiwn tou mexri na vgei mono-psifios einai: ")
print(res)    