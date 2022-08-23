import smtplib  # smtp---->Simple Mail Transfer Protocol....we need server here too(second line code)
import speech_recognition as sr
import pyttsx3 #python text to speech
from email.message import EmailMessage

listener =sr.Recognizer() #to hear our voice
engine= pyttsx3.init() #python engine that speaks to you..init ---> initialize

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.microphone() as source:
            print('listening....')
            voice= listener.listen(source)
            info= listener.recognize_google(voice)  #to convert audio to text
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server= smtplib.SMTP('smtp.gmail.com', 587) #587 is like a source_address
    server.starttls()#tls --->transport layer security
    server.login('logeshlklogi@gmail.com','yourpasswordhere')
    email= EmailMessage()
    email['From']='logeshlklogi@gmail.com'
    email['To']=receiver
    email['subject']=subject
    email.set_content(message)
    server.send_message(email)
    server.sendmail(
                        'logeshlklogi@gmail.com',
                        'logeshkumaran@student.tce.edu',
                        'Hi my another gmail account'            
                )

email_list= {
    'logesh':'logeshkumaran@student.tce.edu',
    'me':'me@email.com',
    'you': 'you@email.com'
}

def get_email_info():
    talk('To whom you want to send email?')
    name= get_info()
    receiver= email_list[name]
    print(receiver)
    talk('what is the subject of your email?')
    subject= get_info()
    talk('Tell me the text in your email')
    message=get_info()

    send_email(receiver, subject, message)

get_email_info()

