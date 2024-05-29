import speech_recognition as sr
from texttovoice import speakandprinttext
import simpleaudio as sa
from sendmail import sendmail
entry = 'entry.wav'
exitt = "exit.wav"

r = sr.Recognizer()

def microphone():
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        wave_obj = sa.WaveObject.from_wave_file(entry)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
        print("Speak now : ")
        
        
        try:
            audio = r.listen(source,None,15)
            print("Processing ...")

            wave_obj = sa.WaveObject.from_wave_file(exitt)
            play_obj = wave_obj.play()
            play_obj.wait_done()  # Wait until sound has finished playing

            text = r.recognize_google(audio)

            text = text.lower()
            print(text)

        except:
            error = "couldn't understand you sirr"
            speakandprinttext(error)
            

    return text


def stt():
    print("Welcome to the speech to text part of CHARLIE")
    text = microphone()
    print(text)
    speakandprinttext("to add more say 'append', to overwrite say 'overwrite' to send it say 'send'")
    while(1):

        choice = microphone()
        if "append" in choice:
            text = text + microphone()
        elif "overwrite" in text:
            text = microphone()
        elif "send" in choice:
            sendmail(text)
            break
        elif "break" in choice:
            break
    

