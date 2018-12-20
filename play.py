import webbrowser
import time
import speech_recognition as sr
from time import ctime
import sqlite3
#import time
import os
import audio_find as find
from win32com.client import constants
from string import punctuation
from collections import Counter
import win32com.client
import training as tr
#from random import randrange
value=0   


def speak(audioString):
    print("B: "+audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)
    
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.energy_threshold=2000  
        r.phrase_threshold = 0.1  
        r.adjust_for_ambient_noise(source,duration=1)
        speak("Say something!")
        audio = r.listen(source,phrase_time_limit=4)
    data = ""
    try:
        print("Audio Recorded")
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio,language='en-IN')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        check=1
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        
    return data.lower()


def remember(q, a):
    connection = sqlite3.connect('chatdata.db')
    cursor = connection.cursor()
    cursor.execute('INSERT OR REPLACE INTO sentences VALUES (?,?)',(q, a))  
    connection.commit()
    speak("your request is being processed!")
    
def search_data(data):
    if data:     
        if "hi" in data or "hello" in data:
            speak("hi how can i help you")
        elif ('time now') in data or ('time') in data or ('the time') in data:
            speak("now time is"+ctime())
        elif "your name" in data :
            speak("My owner calls me billy!!!") 
        elif "dead" in data:
            speak("no, i am just a machine")
        elif "open google" in data:
            url = 'https://www.google.com/'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
        elif "search " in data or "tell me " in data:
            query=data.replace("search ", "")
            query=data.replace("tell me about ", "")
            url = "https://www.google.com.tr/search?q={}".format(query)
            webbrowser.open(url)
        elif "start training" in data or "training" in data or "train" in data:
            tr.training_start()
        elif "remember" in data or "can you remember" in data:
            speak("yes. what do you want me to rembember for you.")
            q = recordAudio()
##            q = "what is " + q
            speak(q)
            a = recordAudio()
##            a = a.replace("my ", "your ")
            remember(q, a)
        elif "go now" in data or "bye" in data or "good bye" in data or "quit" in data:
            quit()
        else:
            find.find_text(data)

# initialization
#time.sleep(2)
speak("Welcome to My Assistant!!!")
while 1:
    data = recordAudio()
    search_data(data)
    
