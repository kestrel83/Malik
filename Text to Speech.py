from gtts import gTTS
from playsound import playsound

#text to convert to speech
text = input("Enter a phrase: ")

#create a text-to-speech object
tts = gTTS(text)

#save the speech as an mp3 file
tts.save("hello.mp3")

#play the mp3 file
playsound("hello.mp3")
