from time import ctime
import time
import os
import sqlite3
from random import randrange
from string import punctuation
from collections import Counter
from win32com.client import constants
import win32com.client



 # create the tables needed by the program
create_table_request_list = [
    'CREATE TABLE words(word TEXT UNIQUE)',
    'CREATE TABLE sentences(Question TEXT UNIQUE, Answer TEXT)'
   ]


def speak(audioString):
    print("B: "+audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)

def training_start():
   # initialize the connection to the database
   connection = sqlite3.connect('chatdata.db')
   cursor = connection.cursor()

   for create_table_request in create_table_request_list:
      try:
        cursor.execute(create_table_request)
      except:
         pass
   speak("wait while training")  
   filne = "data/update.txt"
   f = open(filne, 'r+')
   ques=[]
   ans=[]
   ques_status=0
   while 1:
     lines = f.readlines()
     if not lines:
       break
     for line in lines:
       #print (line)
       if 'Q:'in line:
         ques=line [3:]
         ques_status=1
       elif 'A:'in line and ques_status==1:   
         ans=line [3:]
         print('Q: '+ques)
         print('A: '+ans)
         ques_status=0
         cursor.execute('INSERT OR REPLACE INTO sentences VALUES (?,?)',(ques, ans))  
       else:
        ques_status=0

   f.close()
   connection.commit()
   speak("training of current data completed")  















    
    
    
