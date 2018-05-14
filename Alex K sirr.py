import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("What do you want from me dad?")
    print("Listening...")
    audio = r.listen(source)
    print("thinking...")


try:
    words = r.recognize_google(audio)
    speak.Speak("Ok dad, lets look for " + r.recognize_google(audio))
    wb.open("https://www.youtube.com/results?search_query=" + words)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Regocnition service; {0}".format (e))
