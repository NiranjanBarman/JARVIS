from brain.Aibrain import replybrain
from body.lisen import MicExcution
import datetime
import os
import random
print(">>Starting Jarvis , Please wait")
from body.speak import Speak
from feature.Open import OpenExe

def MicExcaution():
    while True:
        query = MicExcution()
        query = str(query).replace(".","")
        valuereturn = OpenExe(query)
        if valuereturn == True:
            pass

        elif len(query)<2:
            pass
        elif 'music' in query or "play song" in query:
            Speak("sure sir")
            Speak("would you like to play sir")
            
        elif 'interesting ' in query or 'anything' in query or 'another song' in query or 'hit music' in query or 'start' in query :
            Speak("sure sir")
            n=random.randint(0,1)
            music="D:\music_dir"
            files=os.listdir(music)
            d=random.choice(files)
            os.startfile(os.path.join(music,files[n]))
            print("music")      

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Speak(f"Sir, the time is {strTime}")
        reply=replybrain(query)
        Speak(reply)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>= 0 and hour<12:
        Speak("Good Morning Sir")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        Speak(f"the time is {strTime} , Jarvis In Your Service Sir !")
    elif hour>= 12 and hour<18:
        Speak("Good Afternoon Sir")  
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        Speak(f"the time is {strTime} ,Jarvis In Your Service Sir !")
    else:
        Speak("Good Evening Sir") 
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        Speak(f"the time is {strTime} , Jarvis In Your Service Sir !")
    MicExcaution()

wishMe()