import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("pragya you are hot!")
        else:
            speak("welcome darling bobo!")

        speak("how may i help you, pragya darling!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_thresold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"you: {query}\n")

    except Exception as e:
        print(e)
        print("darling repeat kar...")
        speak("darling repeat kar...!")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =10)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")
        
        elif 'play music' in query:
            webbrowser.open("https://music.youtube.com/")



