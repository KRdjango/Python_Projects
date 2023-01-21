import speech_recognition as adam
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import torch


listener=adam.Recognizer()
engine=pyttsx3.init()
engine.say("Hi I am Adam")
engine.say("I am your personal assisstant")
engine.say("And what can I do for you")
engine.runAndWait() 
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with adam.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "adam" in command:
                command=command.replace("adam"," ")
                print(command)      
    except:
        pass
        return command
def run_adam():
    command=take_command()
    print(command)
    command = "play","time", "heck","friend","love"
    if "time" in command:
        t=datetime.datetime.now().strftime("%I : %M  %p")
        print(t)
        talk("Current time is" +t)
    elif "heck" in command:
        info_1=command.replace("heck"," ")
        info=wikipedia.summary(info_1, 10)
        talk(info)
    elif "friend" in command:
        v1="Yes for sure,I am your best friend"
        print(v1)
        talk(v1)
    elif "love" in command:   
        talk("I love you too")
    elif "jokes" in command:
        talk(pyjokes().getjokes())
    else:
        talk("can you please repeat one time")

while True:
    run_adam()


