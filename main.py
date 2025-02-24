import speech_recognition as sr
import pyttsx3
import webbrowser
import music

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()


def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

def processtask(t):
    if "open google" in t.lower():
        webbrowser.open("https://google.com")
        
    elif "open linkedin" in t.lower():
        webbrowser.open("https://www.linkedin.com/in/nigamakrati/")
        
    elif "open instagram" in t.lower():
        webbrowser.open("https://www.instagram.com/")
        
    elif "open youtube" in t.lower():
        webbrowser.open("https://www.youtube.com/")
    
    elif "open spotify" in t.lower():
        webbrowser.open("https://open.spotify.com/")
        
    elif t.lower().startswith("play"):
        song = t.lower().split(" ")[1]
        link = music.m[song]
        webbrowser.open(link)
    

if __name__ == "__main__":
    speak("starting assistant")
    while True:
     # listen the word Zach and obtain audio from microphone
     r = sr.Recognizer()
     recognizer.dynamic_energy_threshold = 5000
     
     print("listening")
     try:
         with sr.Microphone() as source:
          print("processing")
          audio=r.listen(source, timeout=5 , phrase_time_limit=3)
          word = r.recognize_google(audio)
          print(f"Recognized word: {word}")
         if(word.lower()=="assistant"):
             speak("Yes")
            #  get the task
             with sr.Microphone() as source:
                print("assistant is active")
                audio=r.listen(source, timeout=3, phrase_time_limit=2)
                task = r.recognize_google(audio)
                print(f"Recognized task: {task}")
                
                processtask(task)
            
     
     except sr.UnknownValueError:
         print("Could not understand audio")
     
     except sr.RequestError as e:
         print("Error; {0}", format(e))
         
       