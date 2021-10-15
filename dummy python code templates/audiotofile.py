import speech_recognition as sr

AUDIO_FILE=("calimp3.wav") #import the audio file
r=sr.Recognizer() #initialize the recognizer
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    s=r.recognize_google(audio) #store the audio as text in s
except sr.UnknownValueError:
    print("Could't understand the voice")
except sr.RequestError:
    print("Could't get the result")
with open("output.txt","w") as f:
    f.write(s)
f.close()
print("Audio stored in output.txt")