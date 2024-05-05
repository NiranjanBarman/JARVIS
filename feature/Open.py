import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(query):
    query = str(query).lower()

    if "visit" in query:
        Nameofweb = query.replace("visit","")
        Link = "https://WWW.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    elif "open" in query:
        NameotheApp = query.replace("open","")
        pyautogui.press('win')
        sleep(0.5)
        keyboard.write(NameotheApp)
        sleep(0.5)
        keyboard.press('Enter')
        return True



