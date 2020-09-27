# pip install SpeechRecognition
# pip install PyAudio
# python -m speech_recognition  for checking install properly or not  

import speech_recognition  as s

sr=s.Recognizer()

print(" Jarvis is listing ......")

with s.Microphone() as m:

 audio=sr.listen(m)
 z=sr.recognize_google(audio,language='eng-in')
 print(z)