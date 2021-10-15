import speech_recognition as sr

AUDIO_FILE=("audio.wav") #import the audio file
r=sr.Recognizer() #initialize the recognizer
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    print("The audio file contains : "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could't understand the voice")
except sr.RequestError:
    print("Could't get the result")
    