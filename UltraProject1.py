import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser 
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning boss!")
    elif hour>=12 and hour<18:
        speak("good afternoon boss!")
    else:
        speak("good evening sir!")
    speak("i am computer boss. Please tell me how may i help you anirudh singh")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query
if __name__=="__main__":
    wishme()
    if 1:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentances=2)
            speak("according to wikipedia")
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\ashish kumar\\Desktop\\LEYTHAN-X'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[5]))
            
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
            
        elif 'open code' in query:
            codepath=""
            os.startfile(codepath)
        elif 'hello bro' in query:
            speak(f"i am fine boss. how are you boss.")
