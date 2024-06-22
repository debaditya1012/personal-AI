import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "a7f40e8ce83a4bef9883aa6a47dd69d1"
 
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
     elif "open facebook" in c.lower():
          webbrowser.open("https://facebook.com")
     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")
     elif "open linkedin" in c.lower():
          webbrowser.open("https://linkedin.com")
     elif c.lower().startswith("play"):
          song = c.lower().split(" ")[1]
          link = musiclibrary.music[song]    
          webbrowser.open(link)
     elif "news" in c.lower(): 
          r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=a7f40e8ce83a4bef9883aa6a47dd69d1")  
          if r.status_code == 200:
            headlines = r.json()
            articles = headlines.get('articles', [])
            for article in articles:
                 speak(article['title'])

     else:
          #let openAI handle the request
          pass            
            
                    
               
    
if __name__ == "__main__":
    speak("initializing Watson....")
    while True:
        # Listen for the wake word "Arthur"
            # obtain audio from the microphone
            r = sr.Recognizer()
            





          
            print("recognizing....")
            try:
                with sr.Microphone() as source:
                    print("listening...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                if(word.lower() == "watson"):
                     speak("Hi admin")
                     #listen for command
                     with sr.Microphone() as source:
                        print("watson active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

                        

            except Exception as e:
                 print("Error; {0}".format(e))
       

            