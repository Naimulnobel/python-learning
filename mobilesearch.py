# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 13:44:31 2019

@author: Student mct
"""
def isPhoneNumber(text): 
    try:
     if len(text) != 11:       
         return False    
     for i in range(0, 3): 
         if not text[i].isdecimal():           
             return False      
           
         for i in range(4, 7):          
             if not text[i].isdecimal():            
                 return False      
               
             for i in range(8, 11):          
                 if not text[i].isdecimal():            
                     return False     
             return True
    except ValueError:
       print("Oops!  That was no valid number.  Try again...") 
         
message =input()
for i in range(len(message)):
    chunk = message[i:i+11]
    if isPhoneNumber(chunk):
        print('phone number is found:',chunk)