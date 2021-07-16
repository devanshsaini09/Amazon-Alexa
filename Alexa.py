#You need to install these modules
from os import spawnl
import os
from sys import api_version, path
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')                                                                                                                  
# print(voices[1].id)                                                                                                                                   
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    if hour>=12 and hour<18:
        speak("Good Afternoon!")

    if hour>=18 and hour<0:
        speak("Good Evening!")

    speak("Hi, I am Alexa, What can I do for you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  #this is 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")        
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'who are you' in query:
            speak("I am Alexa, Your persnel assistant")
