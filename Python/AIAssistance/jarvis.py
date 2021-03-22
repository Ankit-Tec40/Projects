import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib


engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(time)


def date():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12 :
        speak("Good morning ankit")
    elif hour>=12 and hour<18 :
        speak("Good afternoon ankit")
    else:
        speak("Good evening ankit")

    speak("How can i help you ?")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recogning...")
        query=r.recognize_google(audio,language="en-US")
        print(query)
    except  Exception as e:
        print(e)
        print("say that again...")
        return "None"
    return query

# def sendemail(to,content):
    






if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            print("searching...")
            speak("searching")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "exit" in query:
            exit()

    
