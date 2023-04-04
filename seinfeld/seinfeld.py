import speech_recognition as sr
import time
import pygame

pygame.mixer.init()

def playsound(file):
    sound = pygame.mixer.Sound(file)
    sound.play()
    while pygame.mixer.get_busy():
        pass

seinfeld = ["i like how", "i read a report", "we're so", "we are so", "people are",
        "when you", "i saw", "i'll never understand", "i will never understand",
        "what's the deal with", "what is the deal with", "have you ever noticed",
        "why is it that", "i don't understand why", "i do not understand why", 
        "did you ever notice", "did you ever wonder why", "do you ever wonder why",
        "can you believe that", "it's amazing to me that", "it is amazing to me that",
        "what's up with", "what is up with", "who came up with the idea that",
        "why do they call it"]

r = sr.Recognizer()
mic = sr.Microphone(device_index=1) #use sr.Microphone.list_microphone_names() for index number

while(True):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=1)
        
        try:
            phrase = r.recognize_google(audio).lower()
            
            if(phrase in seinfeld):
                playsound("seinfeld.mp3")
            else:
                pass
            
        except:
            pass

        time.sleep(1)
    
