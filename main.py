import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib, ssl
import nova_request as ai
import image_generation
import mtranslate

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    #audio = mtranslate.translate(audio, to_language="hi", from_language="en-in")
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            #content = mtranslate.translate(content,to_language="en-in")
            print("You Said..........." + content)
        except Exception as e:
            print("Please try again...") 
    return content

def main_process():
    nova_chat = []
    while True:
        request = command().lower()
        if "hello" in request:
            speak("welcome, how can i help you.")
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=q-baNdEnRxs")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=PB8Nt8RZjXw")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=3PP_ri9rS8Y")
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is " + str(now_time))
        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                speak("Adding Task : " + task)
                with open ("todo.txt", "a") as file:
                    file.write(task + "\n")
        elif "speak task" in request:
             with open ("todo.txt", "r") as file:
                 speak("work we have to do today is :" + file.read())
        elif "show work" in request:
            with open ("todo.txt", "r") as file:
                tasks = file.read()
            notification.notify(
                title = "Today's work",
                message = tasks  
            )
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")        
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "wikipedia" in request:
            request = request.replace("nova ", "")
            request = request.replace("search wikipedia ", "")
            print(request)
            result = wikipedia.summary(request, sentences=2)
            print(result)
            speak(result)

        elif "search google" in request:
            request = request.replace("nova ", "")
            request = request.replace("search google ", "")
            webbrowser.open("https://www.google.com/search?q="+request)

        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+917303440366", "Hi", 14, 31)
        # elif "send email" in request:
        #     pwk.send_mail("hemlatagupta171@gmail.com", user_config.gmail_password, "hello", "hello how are you", "kotiyaharshal17@gmail.com")
        
        elif "send email" in request:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("kotiyaharshal17@gmail.com", user_config.gmail_password)
            message = """
            This is the message .

            python code 

            """

            s.sendmail("kotiyaharshal17@gmail.com", "hemlatagupta171@gmail.com", message)
            s.quit()
            speak("email sent")

        elif "image" in request:
            request = request.replace("nova ", "")
            image_generation.generate_image(request)    
            speak("image created")       
        elif "ask ai" in request:
            request = request.replace("nova ", "")
            request = request.replace("ask ai ", "")
            
            print(request)
            response = ai.send_request(request)
            print(response)
            speak(response)

        else:
            request = request.replace("nova ", "")
            
            nova_chat.append(request)
            print(nova_chat)
            response = ai.send_request2(nova_chat)

            nova_chat.append(response)
            print(nova_chat)
            speak(response)

        
if __name__ == "__main__":
    main_process()
