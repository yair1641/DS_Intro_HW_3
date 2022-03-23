

        



# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:12:26 2022

@author: Yair Langerman 204156434
"""
#QA
import os
os.chdir("C:/Users/user/Dropbox/My PC (Yair-Vostro)/Desktop")

#with open("ex3_text.txt","r") as file:
   # for line in file:
       # print(line)


import os.path

def check_file(file):
    file_exists = os.path.exists(file)
    if not file_exists:
        return False
    return True


def check_input(n, file):
    if type(n) != int:
        return False
    return True



def read_line(n, file):
    if not check_input(n, file):
        return "invalid input detected"
    if not check_file(file):
        return "file not found"       
    if type(file)==str:
        newlist= list()
        counter=0
        handle=open(file)
        for line in handle:
            counter=counter+1
            if n==counter: 
                return line
        
        return "line" + n + "doesn't exist"
    else:
        return "file not found"

print(read_line(4,'ex3_text.txt'))


#QB

#import os
#os.chdir("C:/Users/user/Dropbox/My PC (Yair-Vostro)/Desktop")

def check_file2(file):
    file_exists = os.path.exists(file)
    if not file_exists:
        return False
    return True

def check_input2(file):
    if type(file)!= str:
        return False
    return True

def longest_words(file):
   five_longestwords_list=list()
   big_list=[]
   try:
        with open(file,"r") as opentext:
            for line in opentext:
                words=line.split()
                for word in words:
                    big_list.append(word)
            count=0
            while count<5:
                count+=1
                five_longestwords_list.append(max(big_list,key=len))
                big_list.remove(max(big_list,key=len))
            return five_longestwords_list
   except:
       print("file not found")
       return []
print(longest_words("ex3_text.txt"))
                  
