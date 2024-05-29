import speech_recognition as sr
from texttovoice import speakandprinttext
import simpleaudio as sa

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
            audio = r.listen(source,None,5)

            print("Processing ...")

            wave_obj = sa.WaveObject.from_wave_file(exitt)

            play_obj = wave_obj.play()
            play_obj.wait_done()  # Wait until sound has finished playing
            
            text = r.recognize_google(audio)
            text = text.lower()
            print(text)
        except:
            text = "couldn't understand you sirr"
            speakandprinttext(text)
            return '0'

    return text
# microphone()