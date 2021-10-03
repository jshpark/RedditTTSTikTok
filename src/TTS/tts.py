import pyttsx3

engine = pyttsx3.init(driverName='sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)

def Test():
    voices = engine.getProperty('voices')
    print(voices[4].id)
    engine.setProperty('voice', voices[4].id)
    engine.say('The quick brown fox jumped over the lazy dog.')

    engine.runAndWait()

def Read(string):
    engine.say(string)
    engine.runAndWait()