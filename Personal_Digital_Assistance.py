import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150) # Decrease the Speed Rate x2


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning sir!")
        speak("Good morning sir!")
        

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am  Anna your personal assistant . Please tell me can I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def youtubesearch(query1):
    search_item="www.youtube.com/results?search_query="+str(query1)
    return search_item
def googlesearch(query1):
    search_item="www.google.com/search?client=firefox-b-d&q="+str(query1)
    return search_item

if __name__ == "__main__":
    
    check=bool(False)
    state = takeCommand().lower()
    if "wake up anna" in state:
        check=bool(True)
        wishMe()
        intro=1
        trial=1
    while check:
    # if 1:
        if trial != 1:
            time.sleep(5)
        query = takeCommand().lower()
        trial=2
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
           # print('\n')
            #print(results)
            

        elif 'open youtube' in query:
            speak("what do you want to search sir!!!")
            query1 = takeCommand().lower()
            webbrowser.open(youtubesearch(query1))

        elif 'open google' in query:
           speak("what do you want to search sir!!!")
           query1 = takeCommand().lower()
           webbrowser.open(googlesearch(query1))

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com/_patnaik_prasant_01/")   

       
        elif 'play music' in query:
            music_dir = 'F:\\songs'
            songs = os.listdir(music_dir)
            ran=random.randint(0,15)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[ran]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            strday = datetime.datetime.now().strftime("%Y-%m-%d")  
            speak(f"Sir, the date is {strday}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'anna go to sleep' in query:
            print("Thanks sir, hope you have found me helpful and now I am going in recharge mode") 
            speak("Thanks sir, hope you have found me helpful and now I am going in recharge mode") 
            break

        elif 'marry me' in query:
            speak("I am very happy to know that you want to marry me but I am in love with my i 5 proccessor, Hope you will find a better partner than me but I can be you best friend and you can share anything with me.")

        elif 'introduce yourself' in query:
            if intro == 1:
                print("Hi, I am anna,Your personal assistant with 1 giga hertz processing speed and 1.25 terra bytes of storage.I was created on 19th of march 2023 to ease my master's work.I can help you find any google searches, youtube search, find in wikipedia,can tell you time,etc.I am eager to work for you sir....")
                speak("Hi, I am anna,Your personal assistant with 1 giga hertz processing speed and 1.25 terra bytes of storage.I was created on 19th of march 2023 to ease my master's work,I can help you find any google searches, youtube search, find in wikipedia,can tell you time,etc.I am eager to work for you sir....")
                intro=0

        elif 'tell me a joke' in query:
             speak("shuti batshi ho kya?")
