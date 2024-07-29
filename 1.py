import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understood")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            return ""

def speechhtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__":
    data1 = sptext().lower()
    if "your name" in data1:
        name = "My name is Jarvis"
        speechhtx(name)
    elif "how old are you" in data1:
        age = "I am two years old"
        speechhtx(age)
    elif 'now time' in data1:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speechhtx(time)
    elif 'youtube' in data1:
        webbrowser.open('https://www.youtube.com/')
        speechhtx('Opening YouTube')
    elif 'joke' in data1:
        joke_1 = pyjokes.get_joke(language='en', category='neutral')
        speechhtx(joke_1)
    elif 'play song' in data1:
        add = "D:\_Bak"
        listsong = os.listdir(add)
        print(listsong)
        os.startfile(os.path.join(add, listsong[1]))

    elif "exit" in data1:
        speechhtx("Goodbye")
        exit()
    
    else:
        print("Not understood")
