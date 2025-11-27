import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

def speak(text):
    print("Krishna AI:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word 'Krishna'...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print("Heard:", query)
        except Exception as e:
            return ""
        return query.lower()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Krishna AI, your assistant.")

def handle_command(command):
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        query = command.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia:")
            speak(results)
        except:
            speak("Sorry, I couldn't find that on Wikipedia.")

    elif 'open notepad' in command:
        os.system("notepad.exe")

    elif 'open chrome' in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)

    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")

    elif 'time' in command:
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_str}")

    elif 'ram ram' in command or 'quit' in command:
        speak("Goodbye! Have a great day.")
        exit()

def main():
    wish_user()

    while True:
        query = take_command()
        if "krishna" in query:
            speak("Yes, I am listening...")
            command = take_command()
            if command:
                handle_command(command)

if __name__ == "__main__":
    main()
