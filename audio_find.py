import re
import os
import sqlite3
from random import randrange
from string import punctuation
from collections import Counter
from win32com.client import constants
import win32com.client

# initialize the connection to the database
connection = sqlite3.connect('chatdata.db')
cursor = connection.cursor()

# create the tables needed by the program
create_table_request_list = [
    'CREATE TABLE words(word TEXT UNIQUE)',
    'CREATE TABLE sentences(Question TEXT UNIQUE, Answer TEXT)'
]
for create_table_request in create_table_request_list:
    try:
        cursor.execute(create_table_request)
    except:
        pass

def speak(audioString):
    print("B: "+audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)
   
def find_text(string_found):
    
    #print("in find text :"+string_found[1:])  
    rows=cursor.execute("SELECT Answer FROM sentences WHERE Question= '"+string_found[1:]+"'")
    #print(rows[0])
##    f1 = True
    for row in rows:
       print(row[0])
       if(row[0]):
           speak(row[0])
##           f1 = False
           return       
    rows1=cursor.execute("SELECT Answer FROM sentences WHERE Question like '%"+string_found[1:]+"%'")
    
    f2 = True
    for row1 in rows1:
       print(row1[0])
       if(row1[0]):
           f2 = False
           speak(row1[0])
           return
    if f2:
        speak("sorry about that, I'm still learning!!!")
        
        
