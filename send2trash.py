# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:27:32 2019

@author: Student mct
"""
import send2trash
exampleFile=open('example.text','a')
exampleFile.write('\n hahaa')
exampleFile.close()
exampleFile.send2trash('example.text')