import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb



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


    






if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "who are you" in query:
            speak("I am jarvis an AI assistant")
        elif "wikipedia" in query:
            print("searching...")
            speak("searching")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "search in chrome" in query:
            speak("what to search ?")
            chromepath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome.exe %s"
            search=takecommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "exit" in query:
            exit()

    
