# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:09:19 2019

@author: Kostas Ziovas
"""
#------------------Definitions---------------------------#
from random import randint

#----------------Matrix Creation------------------------#
n = 10
m = 10
pinakas = ['_'] * n
k=0
for k in range(n):
    pinakas[k] = ['_'] * m
 

#------------------Functions----------------------------#
def print_mat(pinakas):
    i=0
    for i in range(0,n):
        print(" ",i,end='')
    print()
    for i in range(len(pinakas)):
        print("| ",end='')
        for j in range(len(pinakas[i])):
            print(pinakas[i][j]," ",end='')
        print("|",i) 
     

def comp_move():
    
    c_row=randint(0, n-1)
    c_col=randint(0 ,m-1)
    c_lett=randint(0, 1)
    if (c_lett==0):
        c_lett='O'
    else:
        c_lett='S'
    if(pinakas[c_row][c_col]=='_'):
        pinakas[c_row][c_col]=c_lett
        print("\nO ipologisths dialekse: ")      
        print_mat(pinakas)
        return c_row,c_col
    else:
        return(comp_move())


def player_move():
    gramma=input("Dwse S h O: ")
    if(gramma=='S' or gramma=='O' or gramma=='s' or gramma=='o'):
            gramma=gramma.upper()
            seira=input("Dwse arithmo seiras 0-9: ")
            stilh=input("Dwse arithmo stilhs 0-9: ")
            if(seira.isdigit() and stilh.isdigit()):
                seira=int(seira)
                stilh=int(stilh)
                if(seira>=0 and seira <=(n-1) and stilh>=0 and stilh<=(m-1) and pinakas[seira][stilh]=='_'):
                    pinakas[seira][stilh]=gramma
                    print_mat(pinakas)
                    return seira,stilh
    
                else:
                   print("--!Auth h thesh einai piasmenh dialekse allh!--")
                   return(player_move())
            else:
                print("--!Auto to noumero den einai swsto. Ksanadokimase!--")
                return(player_move())

    else:
        print("--!Auto to simvolo den einai swsto. Ksanadokimase!--")
        return(player_move())


def freespace():
    count=0
    for l in range(0,n):
        for t in range(0,m):
           if(pinakas[l][t]=='_'): 
               count=count+1
    if(count>0):
        return (1)
    elif(count==0):
        return(0)

def check(row,col):
    count=0
    if(pinakas[row][col]=='S'):
        if((row-1)>=0 and pinakas[row-1][col]=='O'):
            if((row-2)>=0 and pinakas[row-2][col]=='S'):
                count=count+1
                      
        if((col-1)>=0 and pinakas[row][col-1]=='O'): 
             if((col-2)>=0 and pinakas[row][col-2]=='S'):
                count=count+1
            
        if((row+1)<=(n-1) and pinakas[row+1][col]=='O'): 
             if((row+2)<=(n-1) and pinakas[row+2][col]=='S'):
                count=count+1
            
        if((col+1)<=(m-1) and pinakas[row][col+1]=='O'):  
             if((col+2)<=(m-1) and pinakas[row][col+2]=='S'):
                count=count+1
             
        if((row+1)<=(n-1) and (col+1)<=(m-1) and pinakas[row+1][col+1]=='O'):  
             if((row+2)<=(n-1) and (col+2)<=(m-1) and pinakas[row+2][col+2]=='S'):
                count=count+1
            
        if((row-1)>=0 and (col-1)>=0 and pinakas[row-1][col-1]=='O'):  
            if((row-2)>=0 and (col-2)>=0 and pinakas[row-2][col-2]=='S'):
                count=count+1 
            
        if((row-1)>=0 and (col+1)<=(m-1) and pinakas[row-1][col+1]=='O'):  
            if((row-2)>=0 and (col+2)<=(m-1) and pinakas[row-2][col+2]=='S'):
                count=count+1
            
        if((row+1)<=(n-1) and (col-1)>=0 and pinakas[row+1][col-1]=='O'):  
            if((row+2)<=(n-1) and (col-2)>=0 and pinakas[row+2][col-2]=='S'):
                count=count+1
            
        else:
            return(count)
            
    elif(pinakas[row][col]=='O'):
        if((row-1)>=0 and (row+1)<=(n-1) and pinakas[row-1][col]=='S' and pinakas[row+1][col]=='S'):
            count=count+1
        if((col-1)>=0 and (col+1)<=(m-1) and pinakas[row][col-1]=='S' and pinakas[row][col+1]=='S'):
            count=count+1
        if((row-1)>=0 and (row+1)<=(n-1) and (col-1)>=0 and (col+1)<=(m-1) and pinakas[row-1][col+1]=='S' and pinakas[row+1][col-1]=='S'):
            count=count+1
        if((row-1)>=0 and (row+1)<=(n-1) and (col-1)>=0 and (col+1)<=(m-1) and pinakas[row+1][col+1]=='S' and pinakas[row-1][col-1]=='S'):
            count=count+1
        else:
            return(count)
    return(count)
                
#---------------------------------------------------------------------------------#
#-------------------------Main Program--------------------------------------------#
#---------------------------------------------------------------------------------#
   
print("----------------------------------------------")
print("----|||| KALOSIRTHES STO PAIXNIDI: SOS ||||----")
print("----------------------------------------------")

gameon='p'
plscore=0
comscore=0
print_mat(pinakas)
while(gameon!='e' and freespace()>0):
    pr,pc=player_move()
    plcheck=check(pr,pc)
    plscore=plscore+plcheck

    
    if(freespace()==0):
        break
    
    cr,cc=comp_move()
    cocheck=check(cr,cc)
    comscore=comscore+cocheck
    print("--------------------------------------")
    print("To score tou paixth: ",plscore)
    print("To score tou ipologisth: ",comscore)
    print("--------------------------------------")
    gameon=input("Gia termatismo pata to e,alliws opoiodipote allo simvolo: ")


print("--------------------------------------")
print("To score tou paixth: ",plscore)
print("To score tou ipologisth: ",comscore)
print("--------------------------------------")    
print("Euxaristoume pou peksate!")




 
