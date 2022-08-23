import pyttsx3 #python text to speech
engine= pyttsx3.init() #python engine that speaks to you..init ---> initialize

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('To whom you want to send email?')

