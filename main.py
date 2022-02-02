import speech_recognition as sr #ovo je za prepoznavanje govora
from gtts import gTTS # ovo je google API za pretvaranje teksta u govor
import os #ovo je za cuvanje datoteka i otvaranje
import playsound #ovo je za pustanje zvukova koje imamo sacuvano na kompjuteru 
from selenium import webdriver # za kontrolu browser-a 
import wolframalpha # za racunski deo koda

num = 0 

def speak(text):
    za_govor = gTTS(text=text, lang='en')
    filename = str(num)+".mp3" 
    za_govor.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    slusalac = sr.Recognizer()
    with sr.Microphone() as source:
        audio = slusalac.listen(source)
        rekao = ""

        try:
            rekao = slusalac.recognize_google(audio)
            print(rekao)
        except Exception as e:
            print("GRESKA-> " + str(e))
    return rekao

# def search_web(input):
      
#     driver = webdriver.Chrome(executable_path= "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#     driver.implicitly_wait(1)
#     driver.maximize_window()
  
#     if 'youtube' in input.lower():
  
#         speak("Opening in youtube")
#         indx = input.lower().split().index('youtube')
#         query = input.split()[indx + 1:]
#         driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
#         return
  
#     elif 'wikipedia' in input.lower():
  
#         speak("Opening Wikipedia")
#         indx = input.lower().split().index('wikipedia')
#         query = input.split()[indx + 1:]
#         driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
#         return
  
#     else:
  
#         if 'google' in input:
  
#             indx = input.lower().split().index('google')
#             query = input.split()[indx + 1:]
#             driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
#         elif 'search' in input:
  
#             indx = input.lower().split().index('google')
#             query = input.split()[indx + 1:]
#             driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
#         else:
  
#             driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))
  
#         return

def otvori_aplikaciju(input):
      
    if "chrome" in input:
        speak("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return
  
    elif "word" in input:
        speak("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return
  
    elif "excel" in input:
        speak("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return
    elif "brave" in input:
        speak("Opening Brave browser")
        os.startfile('C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe')
        return
    
    else:
  
        speak("Application not available")
        return

def process_text(input):
    try:
        # if 'search' in input or 'play' in input:
        #     search_web(input.lower())
        #     return
  
        if "who are you" in input or "define yourself" in input:
            odgovor = '''Hello, I am Katarina. Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as calculating sums or opening applications etcetra'''
            
            speak(odgovor)
            return
  
        elif "who made you" in input or "created you" in input:
            odgovor = "I have been created by Aleksa, Andrea and Lena."
            speak(odgovor)
            return

  
        elif "calculate" in input.lower():
              
            # u ovom delui smo uneli moj id za wolpframalpha API za racunanje, ovo samo radi za kada mu se kaze calculate
            app_id = "56RVRT-3T6YLGPQQX" 
            client = wolframalpha.Client(app_id)
  
            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak("The answer is " + answer)
            return
  
        elif 'open' in input:
            # za otvaranje aplikacija
            otvori_aplikaciju(input.lower()) 
            return
  
        else:
  
            speak("I do not understamd, try again!")
            return
            # speak("I can search the web for you, Do you want to continue?")
            # ans = get_audio()
            # if 'yes' in str(ans) or 'yeah' in str(ans):
            #     search_web(input)
            # else:
            #     return
    except :
        speak("I did not quite catch that, please try again!")
        # speak("I don't understand, I can search the web for you, Do you want to continue?")
        # ans = get_audio()
        # if 'yes' in str(ans) or 'yeah' in str(ans):
        #     search_web(input)


#MAIN FUNKCIJA
if __name__ == "__main__":
    speak("What's your name, Human?")
    name ='Human'
    name = get_audio()
    speak("Hello, " + name + '.')
      
    while(1):
  
        speak("What can i do for you?")
        text = get_audio().lower()
  
        if text == 0:
            continue
  
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            speak("Ok bye, "+ name+'.')
            break
        process_text(text)