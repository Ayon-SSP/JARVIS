import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Hi! I'm Jarvis")

MASTER = "Ayon..........."

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# speak function will pronounce the string which is pass to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per the current time
# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#
#     if hour >= 0 and hour < 12:
#         speak("Good Morning" + MASTER)
#
#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon" + MASTER)
#
#     else:
#         speak("Good Evening" + MASTER)
#
#     speak("Hi!I'm Jarvis. How may I help you?")


# Thish function will take comand from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    
    return query


# Main program starts hear...
speak("Initializing Jarvis...")
# wishMe()
query = takeCommand()

# Logic for executing tasks as per the query
if 'wikipedia' in query.lower():
    speak('searching wikipesea...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    # webbrowser.open("youtube.com")
    url = "youtube.com"
    chrome_path = ' '
    print("opening youtube for You.....")
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    # webbrowser.open("google.com")
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'i love you' in query.lower():
    # speak("i love u too ayon....")
    speak("i love u too ")
elif 'you are wast' in query.lower():
    speak("I don't know it is ayon's mistake")
    print("I don't know it is ayon's mistake")
elif 'Do you know my name' in query.lower():
    speak("you are my best friend how can I not know you are name ayon....")

elif 'open my blog' in query.lower():
    # webbrowser.open("google.com")
    url = "https://www.google.com/search?q=karmakaraayon&sxsrf=ALeKk00zBkTefnqO8-dqFl6NtAVmd32-nA%3A1621777972093&ei=NF6qYOGoBbPjz7sP3c-SeA&oq=karmakaraa&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzIECCMQJzIECAAQDTIECAAQDTIECAAQDTIGCAAQDRAKMgYIABANEAoyBAgAEA0yBggAEA0QCjIGCAAQDRAeOgcIABCwAxANOgUILhCRAjoFCC4QsQM6AgguOggILhCxAxCDAToFCAAQkQI6CAgAELEDEIMBOggIABCxAxCRAjoFCAAQsQM6AggAOggILhDHARCvAToECAAQCjoECAAQHlCKE1jXImC9LmgDcAB4AYAB1ASIAZAZkgELMC4zLjUuMS4wLjKYAQCgAQGqAQdnd3Mtd2l6yAEBwAEB&sclient=gws-wiz"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'my photos from google' in query.lower():
    # webbrowser.open("google.com")
    url = "https://www.google.com/search?q=karmakaraayon&sxsrf=ALeKk02mPmg0nbbSucfv4PIId_gI07Wfaw:1621777979834&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiXvpHj-d_wAhUlieYKHVUNC1UQ_AUoA3oECAEQBQ&biw=1707&bih=844&dpr=1.13"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'my profile' in query.lower():
    # webbrowser.open("google.com")
    url = "https://www.linkedin.com/in/ayon-k/"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open reddit' in query.lower():
    # webbrowser.open("google.com")
    url = "reddit.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\admin\\Music\\a"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'pdf' in query.lower():
    url = "file:///E:/MY%20BAG/books/PythonNotesForProfessionals%20(1)%20(1)%20(1)%20(1)%20(2)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1).pdf"
    webbrowser.open_new(url)
elif 'game' in query.lower():
    import random

    print("There will be 9 rounds")
    print("Who will score more he will be the winner")
    print("1)Rock\n2)Paper\n3)Scissor\n")

    score_of_user = 0
    score_of_system = 0


    def opt_of_system():
        if (system == 1):
            print("Rock", end=" ")
        elif (system == 2):
            print("Paper", end=" ")
        elif (system == 3):
            print("Scissor", end=" ")


    def opt_of_user():
        if (user == 1):
            print("Rock")
        elif (user == 2):
            print("Paper")
        elif (user == 3):
            print("Scissor")


    round_number = 1

    while (round_number <= 9):
        print("This is a", " round", round_number)

        user = int(input())
        while (user >= 4):
            print("only Rock, Paper, Scissor  \nNo 4th opt")
            print("cotinue")
            user = int(input())

        system = random.randint(1, 3)
        
        if (system == user):
            opt_of_system()
            print(end=" ------ ")
            opt_of_user()
            print("Draw")
            print("this round is draw so no round is counted")
            print((10 - round_number), " Roundes left")


        elif ((system == 1 and user == 2) or (system == 2 and user == 3) or (system == 3 and user == 1)):
            opt_of_system()
            print(end=" ------ ")
            opt_of_user()
            print("✨-winner of this round-✨")
            score_of_user = score_of_user + 1
            print((9 - round_number), " Roundes left")
            print("U R score is", score_of_user)
            round_number = round_number + 1

        elif ((user == 1 and system == 2) or (user == 2 and system == 3) or (user == 3 and system == 1)):
            opt_of_system()
            print(end=" ------ ")
            opt_of_user()
            print("👎--Loose this round")
            score_of_system = score_of_system + 1
            print((9 - round_number), " Roundes left")
            print("U R score is", score_of_user)
            round_number = round_number + 1
        print(" ")

    if (score_of_user > score_of_system):
        print("👑----✨YOU ARE THE WINNER✨--🌀")

    elif (score_of_user < score_of_system):
        print(f"BETTER LUCK NEXT {MASTER}")

elif 'open vs code' in query.lower():
    codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
    os.startfile(codePath)
    print("VS CODE in ayon's pc")

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}....................Come on..................... hurry up")

elif 'code' in query.lower():
    codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
    os.startfile(codePath)
    print("VS CODE in ayon's pc")