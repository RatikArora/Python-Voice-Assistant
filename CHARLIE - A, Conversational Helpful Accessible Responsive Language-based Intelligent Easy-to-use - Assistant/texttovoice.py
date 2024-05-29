import pyttsx3

def speakandprinttext(command):
    print(command)
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.setProperty('rate',180)
    # engine.setProperty('volume',0.5)
    # engine.save_to_file(command,"this.mp3")
    engine.say(command)
    engine.runAndWait()

