'''
write a code  will take  input as your name and greet you with
good morning , good evening , goodafter noon , good night as per the current time your system :
'''

import pyttsx3
import webbrowser
import speech_recognition as sr
import datetime
import time


a=input("Enter your name =")

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning! ')
        speak(a)

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon! ')
        speak(a)

    if currentH >= 18 and currentH !=0:
        speak('Good Evening! ')
        speak(a)    

greetMe()






        

