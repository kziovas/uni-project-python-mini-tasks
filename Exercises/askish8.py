# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:05:27 2019

@author: Kostas Ziovas
"""

#-----Library calls----#
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

#---------Definitions--------#
url="https://akispetretzikis.com/el/categories/zymarika/garidomakaronada"
html = urlopen(url).read()
soup = BS(html,"lxml")

#-------------------------------------------------------------------------#
#---------------------Main Program----------------------------------------#

#------------------ Erwtima 1: Titlos istoselidas ------------------------#
print("----------------------------------------------")
print("Erwtima 1. O titlos tis selidas einai: ")
print(soup.title.string)
print()

#--------- Erwtima 2: Arithmos <h1>,<h2>, kai <h3> headers ---------------#
print("----------------------------------------------")
count1=len(soup.find_all("h1"))
count2=len(soup.find_all("h2"))
count3=len(soup.find_all("h3"))
#count1=text.count("<h1")
print("Erwtima 2. O arithmos twn headers einai ")
print("<h1>: ",count1,", <h2>: ",count2,", <h3>: ",count3)
print()

#---------- Erwtima 3: Arithmos allagwn grammhs apo <br> ----------------#
print("----------------------------------------------")
countbr=len(soup.find_all("br"))
print("Erwtima 3. O arithmos allgwn grammhs apo <br>")
print("<br>: ",countbr)