import os
import speech_recognition as sr

def takeCommand():

    #It takes microphone input from the user and returns string output



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

while True:
    
    wake_up = takeCommand()

    if 'start' in wake_up:
        os.startfile("C:\\Users\\user\\Documents\\Jarvis\\jarvis.py")

    else:
        print("Nothing......")