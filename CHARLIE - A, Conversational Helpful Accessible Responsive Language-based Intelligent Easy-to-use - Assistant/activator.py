import speech_recognition as sr
from main1 import main1
from texttovoice import speakandprinttext

r = sr.Recognizer()

def charlie():
    while(1):
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.5)
            print("listening")

            try:
                audio = r.listen(source,None,3)
                print("stopping")
                text = r.recognize_google(audio)
                text = text.lower()
                print(text)
                if 'charli' in text or ' ali ' in text or "alexa" in text:
                    speakandprinttext('hmmm')
                    main1()
                elif "terminate" in text :
                    break
                    
            except:
                print("O_o")
            # charlie()




