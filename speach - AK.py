import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb
speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak(".")

"""
answer = pg.prompt("enter your answer")

if answer == "":
    speak.Speak("")

elif answer == "yes":
    speak.Speak("baseball is super cool")

else:
    speak.Speak("You like the color " )

speak.Speak ("What kind of video whould we watch?")
video = pg.prompt("Enter video below.")
speak.Speak("OK, let's look for "  + video + " on YouTube and see what we find.")
wb.open("https://www.youtube.com/results?search_query=" + video)

"""
