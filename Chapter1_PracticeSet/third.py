# The line below is for importing pyttsx3 library
import pyttsx3
engine = pyttsx3.init()
# The lines below change voice of narrator
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
# This function iterates what we write
engine.say("This is the use of pyttsx3 an external library of python")
engine.runAndWait()