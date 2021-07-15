from email import message
from email.mime import text
from typing import Text
from cv2 import data
import pyttsx3
from requests.api import head, request  #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser as web
import os
import smtplib
from email.message import EmailMessage, MIMEPart
import sys
import requests
from bs4 import BeautifulSoup
import time
import pyautogui
import cv2
import numpy as np
import PyPDF2
import operator
import keyboard
import pywhatkit
import pyjokes
import random
import bs4
from pytube import YouTube
from tkinter import Button, Entry, Label, Tk
from tkinter import StringVar
from PyDictionary import PyDictionary as diction
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from googletrans import Translator


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 175)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:    
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def pdf_reader():
    book = open('C:\\Users\\user\\Documents\\Jarvis\\pdf\\thebodyweightwarriorebookv2pdf_compress.pdf','rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speak(f"Total number of pages in this book are {pages}.")
    speak("Sir Please enter the page number for me to read")
    pg = int(input("Pls enter the page number: "))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=50bf4c93fca5473cb9f6ea222b72a4a6"

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]

    head = []
    day=['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth']
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"Today's {day[i]} news is {head[i]}")

def Corona(Country):

    countries = str(Country).replace(" ","")

    url = f"https://worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_='maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovered = Data

    speak(f"Cases : {cases}")
    speak(f"Deaths : {Death}")
    speak(f"Recovered : {recovered}")

def WhatsApp():
    speak("Tell me the name of the person you want to send the message")
    name = takeCommand()
    if 'users-name' in name:
        speak("Tell me the nessage!")
        msg = takeCommand()
        speak("Tell me the time sir")
        speak("Time in hour!")
        hour = int(takeCommand())
        speak("Time in minutes!")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+96892636335",msg,hour,min,20)
        speak("Ok sir, Sending WhatsApp message!")
    else:
        speak("Tell me the phone number")
        phone = int(takeCommand())
        ph = 'country code' + phone
        speak("Tell me the nessage!")
        msg = takeCommand()
        speak("Tell me the time sir")
        speak("Time in hour!")
        hour = int(takeCommand())
        speak("Time in minutes!")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
        speak("Ok sir, Sending WhatsApp message!")  

def Music():
    speak("Tell me the name of the song")
    musicName = takeCommand()
    query = takeCommand().lower()
    if 'play music' in query:
        music_dir = 'C:\\Users\\user\\Pictures\\Music'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))
    else:
        pywhatkit.playonyt(musicName)
    speak("Your song has been played. Enjoy it!")

def ChromeAuto():
    speak("Chrome Automation Activated")
    command = takeCommand()
    if 'close the tab' in command:
        keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')

    elif 'back page' in command:
        keyboard.press_and_release('alt + Right Arrow')

    elif 'forward page' in command:
        keyboard.press_and_release('alt + Left Arrow')

    elif 'everything' in command:
        keyboard.press_and_release('ctrl + a')

    elif 'history' in command:
        keyboard.press_and_release('ctrl + h')

    elif 'downloads' in command:
        keyboard.press_and_release('ctrl + j')

    elif 'window' in command:
        keyboard.press_and_release('ctrl + n')

def Dict():
    speak("Tell me the word you need the meaning to example: what is the meaning of yourword")
    probl = takeCommand()
    if 'meaning' in probl:
        probl = probl.replace("what is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("meaning of","")
        result = diction.meaning(probl)
        speak(f"The meaning of {probl} is {result}")

def TaskExecution():
    speak("verifying user")
    pyautogui.press('esc')
    speak("Verification is sucessful")
    speak("Welcome back.")
    wishMe()

    #def Music():
    #    speak("Tell me the name of the song")
    #    musicName = takeCommand()
    #    query = takeCommand().lower()
    #    if 'play music' in query:
    #        music_dir = 'C:\\Users\\user\\Pictures\\Music'
    #        songs = os.listdir(music_dir)
    #        print(songs)    
    #        os.startfile(os.path.join(music_dir, songs[0]))
    #    else:
    #        pywhatkit.playonyt(musicName)
#
    #    speak("Your song has been played. Enjoy it!")
#
 ################################################################################################################################################################         
#
    #def ChromeAuto():
    #    speak("Chrome Automation Activated")
    #    command = takeCommand()
    #    if 'close the tab' in command:
    #        keyboard.press_and_release('ctrl + w')
#
    #    elif 'open new tab' in command:
    #        keyboard.press_and_release('ctrl + t')
#
    #    elif 'back page' in command:
    #        keyboard.press_and_release('alt + Right Arrow')
    #
    #    elif 'forward page' in command:
    #        keyboard.press_and_release('alt + Left Arrow')
    #
    #    elif 'everything' in command:
    #        keyboard.press_and_release('ctrl + a')
#
    #    elif 'history' in command:
    #        keyboard.press_and_release('ctrl + h')
#
    #    elif 'downloads' in command:
    #        keyboard.press_and_release('ctrl + j')
#
    #    elif 'window' in command:
    #        keyboard.press_and_release('ctrl + n')
#
    #def Dict():
    #    speak("Dictoinary Activated")
    #    speak("Tell me the word you need the meaning to example: what is the meaning of yourword")
    #    probl = takeCommand()
    #    if 'meaning' in probl:
    #        probl = probl.replace("what is the","")
    #        probl = probl.replace("jarvis","")
    #        probl = probl.replace("meaning of","")
    #        result = diction.meaning(probl)
    #        speak(f"The meaning of {probl} is {result}")

    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

  #      elif 'chrome' in query:
  #          ChromeAuto()

        elif 'command' in query:
            os.startfile('C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.exe')

        elif 'music' in query:
            Music()

        elif 'WhatsApp' in query:
            WhatsApp()

        elif 'open youtube' in query:
            web.open("youtube.com")

        elif 'google search' in query:
            speak("This is what I found for you")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("Done Sir!")

        elif 'website' in query:
            speak("Ok sir, Launching....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            web.open(web2)
            speak("Launched!")

        elif 'youtube search' in query:
            speak("Ok sir, this is what i found for you")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            query = query.replace(" ", "")
            webs = 'https://www.youtube.com/results?search_query' + query
            web.open(webs)
            speak("Done Sir")

        elif  'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'start notepad' in query:
            npad = "C:\\Windows\\system32\\notepad.exe"
            speak("Starting Notepad Sir")
            os.startfile(npad)

        elif 'start code' in query or 'visual studio' in query:
            vs = "C:\\Users\\user\\Desktop\\Visual Studio Code.exe"
            speak("Starting Visual Studio Code sir")
            os.startfile(vs)

        elif 'close code' in query or 'visual studio' in query:
            speak("closing Visual Studio Code sir")
            os.system("TASKKILL /F /im Visual Studio Code.exe")

        elif 'close notepad' in query:
            speak("Closing Notepad Sir")
            os.system("TASKKILL /F /im notepad.exe")

        elif 'where are we' in query or 'where am i' in query:
            speak("Wait sir let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json
                city = geo_data['city']
                country = geo_data['Country']
                speak(f"sir I am not sure but according to the information we are in {city} city of {country} country")
            except Exception as e:
                speak('Sorry sir due to an network error i am not able to find where we are')
                pass

        elif 'take screenshot' in query or 'screenshot' in query:
            speak("Sir, please tell me the name of the screenshot file")
            name = takeCommand().lower()
            speak("sir, please hold the screen for a few seconds i am taking the screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done taking the screenshot sir. You may access the screenshot here")

        elif 'how are you' in query:
            speak("I am fine sir, what about you")

        elif 'also good' in query:
            speak("Thats great to hear sir.")

        elif 'fine' in query:
            speak("Thats great to hear sir.")

        elif 'thanks' in query or 'thank you' in query:
            speak("its my plessure sir.")

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute volume' in query:
            pyautogui.press("volumemute")

        elif 'alarm' in query:
            speak("Sir please tell me the time to set alarm. For example set alarm to 5:30 am")
            tt = takeCommand()
            tt = tt.replace("set alarm to", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)

        elif 'you can sleep' in query or 'sleep' in query or 'sleep now' in query:
            speak("Ok sir, I am going to sleep you can call me anytime.")
            break

        elif 'internet speed' in query:

            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir we have{dl} bit per second downloading speed and {up} bit per second uploading speed.")
            print(f"Sir we have{dl} bit per second downloading speed and {up} bit per second uploading speed.")

        elif 'read pdf' in query:
            pdf_reader()

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt") 

 #       elif 'dictionary' in query:
 #           speak("Dictionary Activated")
 #           speak("Tell me the word you need the meaning to example: what is the meaning of yourword")
 #           probl = takeCommand()
 #           if 'meaning' in probl:
 #               probl = probl.replace("what is the","")
 #               probl = probl.replace("jarvis","")
 #               probl = probl.replace("meaning of","")
 #               result = diction.meaning(probl)
 #               speak(f"The meaning of {probl} is {result}")

        elif 'news' in query:
            speak("Please wait sir, I am finding the latest news for you")
            news()

        elif 'email to name' in query:
            speak("Sir what should I say")
            query = takeCommand().lower()
            if "send a file" in query:
                email = "your email"
                password = "your password"
                send_to_email = 'senders email'
                speak("Ok isr, what is the subject for this email?")
                query = takeCommand().lower()
                subject = query
                speak("And sir, what is the message for this email")
                query2 = takeCommand().lower()
                message = query2
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("Pls enter the path of the file here:")

                speak("Please wait I am sending this email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Dispution', "attachment; filename= %s" % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit
                speak("Email has been sent to Lavya")

            else:

                email = "your mail"
                password = "your password"
                send_to_email = 'senders mail'
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit
                speak("Email has been sent to 'senders name'")                 

        elif 'temperature' in query:

            search = "temperature in muscat"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'do some calculations' in query or 'calculation' in query or 'calculate' in query:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Sir, What do you want to calculate, example 3 plus 3")
                    print("Listening...")
                    r.pause_threshold = 1
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,
                }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("Your result is")
                speak(eval_binary_expr(*(my_string.split())))

            except Exception as e:
                print("Pls say that again....")
                speak("Please say that again")
                return "None"
            return query

        elif 'pause' in query:
            keyboard.press('space bar')
        
        elif 'restart' in query:
            keyboard.press('0')       

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'fullscreen' in query:
            keyboard.press('f')

        elif 'theater' in query:
            keyboard.press('t')

        elif 'miniplayer' in query:
            keyboard.press('i')

        elif 'chrome' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'speak game' in query:
            speak("Speak sir I will repeate whatever you say!")
            jj = takeCommand()
            speak({jj})

        elif 'dictionary' in query:
            Dict()

        elif 'download' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube video downloader")
            speak("Enter Video Url Here!")

            Label(root,text= "Youtube Video Downloader",font='arial 15 bold').pack()
            link = StringVar()
            Label(root,text="Paste YouTube Url here:",font='arial 15 bold',).place(x=160,y=60)
            Entry(root, width = 70, textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download("C:\\Users\\user\\Documents\\Jarvis\\Downloads")
                Label(root, text="Downloaded",font = "arial 15").place(x=180,y=210)

            Button(root,text = "Download",font = "arial 15 bold", bg = 'pale violet red', padx = 2, command = VideoDownloader).place(x=180, y=150)

            root.mainloop()
            speak("Video Downloaded")

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("jarvis","")
            speak("You told me to remind you that:"+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close

        elif 'search' in query:
            import wikipedia as googlescrap
            rememberMsg = query.replace("google search","")
            rememberMsg = rememberMsg.replace("jarvis","")
            speak("This is what I found on the web")
            pywhatkit.search(query)

            try:
                result = googlescrap.summary(query,3)
                speak(result)

            except:
                speak("Please say that again")

        elif 'chat bot' in query:

            speak("Chat bot enabled")
            from chatbot import ChatterBot

            reply = ChatterBot(query)

            speak(reply)

            Hello = ('hello','hey','hii','hi')

            reply_Hello = ('Hello Sir , I Am Jarvis .',
                        "Hey , What's Up ?",
                        "Hey How Are You ?",
                        "Hello Sir , Nice To Meet You Again .",
                        "Of Course Sir , Hello .")

            Bye = ('bye','exit','sleep','go')

            reply_bye = ('Bye Sir.',
                        "It's Okay .",
                        "It Will Be Nice To Meet You .",
                        "Bye.",
                        "Thanks.",
                        "Okay.")

            How_Are_You = ('how are you','are you fine')

            reply_how = ('I Am Fine.',
                        "Excellent .",
                        "Moj Ho rhi Hai .",
                        "Absolutely Fine.",
                        "I'm Fine.",
                        "Thanks For Asking.")

            nice = ('nice','good','thanks')

            reply_nice = ('Thanks .',
                        "Ohh , It's Okay .",
                        "Thanks To You.")

            Functions = ['functions','abilities','what can you do','features']

            reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
                        'I Can Call Your G.F .',
                        'I Can Message Your Mom That You Are Not Studing..',
                        'I Can Tell Your Class Teacher That You Had Attended All The Online Classes On Insta , Facebbook etc!',
                        'Let Me Ask You First , How Can I Help You ?',
                        'If You Want Me To Tell My Features , Call : Print Features !')

            sorry_reply = ("Sorry , That's Beyond My Abilities .",
                            "Sorry , I Can't Do That .",
                            "Sorry , That's Above Me.")

            def ChatterBot(Text):
            
                Text = str(Text)

                for word in Text.split():
                
                    if word in Hello:
                    
                        reply = random.choice(reply_Hello)

                        return reply

                    elif word in Bye:
                    
                        reply = random.choice(reply_bye)

                        return reply

                    elif word in How_Are_You:
                    
                        reply_ = random.choice(reply_how)

                        return reply_

                    elif word in Functions:
                    
                        reply___ = random.choice(reply_Functions)

                        return reply___

                    else:
                    
                        return random.choice(sorry_reply)

        elif 'corona' in query or 'coronavirus' in query:

            try:
                speak("Which countries corona cases do you want to know?")

                cccc = takeCommand()

                Corona(cccc)

            except:

                speak("Pls say the countries name again")
        

if __name__ == "__main__":

    while True:
#   speak("Please tell me the password")
        permission = takeCommand()
#   Pass(permission)
        if "wake up" in permission:
            TaskExecution()

        elif "goodbye" in permission or "bye" in permission:
            speak("bye bye sir!")
            sys.exit()
    
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 1

names = ['', 'Lavya', 'Arti', 'Ashish'] #write you name here as , 'name' replace name with your name


cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam.set(3, 640) #set video frame width  
cam.set(4, 480) #set video frame height


minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img = cam.read()
    
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        converted_image,
        scalefactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
    )

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,225,0), 2)

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

        if (accuracy < 100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            TaskExecution()

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (225,225,225), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (225,225,0), 1)

    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff
    if k == 27: #press esc to stop
        break

print("Thankyou for using the program, have a good day!")
cam.release()
cv2.destroyAllWindows()

#####################################################################################################################################################################################

#
#    password = "python"
#
#    passs = str(password)
#
#    if passs==str(password_input):
#
#       speak("Access granted")
#
#    else:
#        speak("Access denied") 









##Get this f**king code viral
