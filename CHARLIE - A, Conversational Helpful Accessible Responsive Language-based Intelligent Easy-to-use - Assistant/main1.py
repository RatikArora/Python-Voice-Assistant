from speechtotext import microphone
from texttovoice import speakandprinttext
from datetime import date,timedelta,datetime
import webbrowser
from websearch import googlesearch
from appopeneer import appopen,appclose
from wiki import wiki
from news import news
import random
from stt import stt

def greetings():
    speakandprinttext("hhhello sir, how can i help you now ?")

def tareek(n):
    din =  date.today()
    if n == 1:
        din = din + timedelta(1)
        speakandprinttext(f"tomorrow is : {din.strftime('%B %d, %Y')} sir !") 
    else:
        speakandprinttext(f"today's date is : {din.strftime('%B %d, %Y')} sir !")
    
def samay():
    waqt = datetime.now().time().strftime("%H:%M")
    speakandprinttext(f"its {waqt}")


def opensite(url):
    print(url)
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open_new_tab(url)


def main1():
    
    while(1):
        # greetings()
        text = microphone()
        print(text)
        if text == '0':
            pass
    

        elif "who are you" in text:
            speakandprinttext("Hello, my name is Charlie. I am a virtual assistant designed to help you with various tasks. I am language-based and capable of understanding natural language input, which means you can interact with me in a natural and conversational manner. I am here to assist you with your daily tasks, provide you with useful information, and make your life easier. Please feel free to ask me anything, and I will do my best to help you.")
        # if "s" in text:
        #     text = text.replace('s','')
        #     print(text)
        elif "charlie" in text :
            speakandprinttext("i am exactly : C.H.A.R.L.I.E - A, Conversational Helpful Accessible Responsive Language-based Intelligent Easy-to-use - Assistant")
        
        elif "i love you" in text:
            speakandprinttext("buddy i have access to your google history, think before you speak baby!")

        elif "date" in text :
            if "tomorrow" in text:
                tareek(1)
            else : 
                tareek(0)

        elif 'time' in text:
            samay()

        elif "joke" in text:
            file = open("jokes.txt",'r',encoding="utf8")
            file = file.readlines()
            joke = random.choice(file)
            speakandprinttext(joke)

        elif "open" in text and "site" in text:
            text = text.replace("open",'')
            text = text.replace("site",'')

            opensite(text)
        elif 'launch' in text or "open" in text:
            if "open" in text:
                text = text.replace("open",'')
            elif 'launch' in text:
                text = text.replace("launch",'')
            
            speakandprinttext("opening "+text)
            appopen(text)

        elif "google" in text or 'tell me' in text:
            if "google" in text:
                text = text.replace("google ",'')
            elif 'tell me' in text:
                text = text.replace("tell me",'')

            speakandprinttext("googling "+text)
            googlesearch(text)

        elif "speech to text" in text or "convert to text" in text or " stt " in text:
            stt()

        elif "news" in text:
            news()

        elif "close" in text:
            text = text.replace("close ",'')
            speakandprinttext("closing"+text)
            appclose(text)

        

        elif "who " in text or "what " in text or "wikipedia " in text:
            if "who is" in text:
                text.replace('who is','')
            elif "what is" in text:
                text.replace('what is','')
            elif "wikipedia" in text:
                text.replace('wikipedia','')

            speakandprinttext(wiki(text))

            
        elif "bye" in text or 'ok' in text or 'okay' in text or 'thank you' in text:
            # charlie()
            return
            
        else:
            print("out of context")

