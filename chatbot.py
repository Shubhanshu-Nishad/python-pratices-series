# pip install SpeechRecognition
# pip install PyAudio
# pip install win32com
# python -m speech_recognition  for checking install properly or not  
# re type statement if you are getting error , & you code code right.

import random
import speech_recognition  as s
from win32com.client import Dispatch

def speak(str):
    speak= Dispatch(("SAPI.SpVoice"))
    speak.speak(str)



hellow = ["hi","is anyone there?", "hello", "good day","hello there"]
bye = ["hi","cya", "see you later","bye" ,"goodbye", "i am Leaving", "have a Good day"]
howare = ["hi","how are you","whats up","how you doing"]
name = ["hi","whats your name","what is your name","do you have any name","what should i call you","name"]
menu = ["i want to buy something", "what is on the menu", "what do you reccommend?", "could i get something to eat"]
hours = ["when are you guys open", "what are your hours", "hours of operation","time","work time","time period"]

print("*******************************************************\n")
print(" Jarvis is listing ......")

while True:
	sr=s.Recognizer()
	# a = input('User said -')
	with s.Microphone() as m:
	#  audio=sr.listen(m)   copy statement not works everywhere
    #  z=sr.recognize_google(audio,language='eng-in')
	 audio = sr.listen(m)
	 a = sr.recognize_google(audio,language='eng-in')

    # print('User Input-'+ z)
	print('user Input - ' + a)

	if a.lower() in hellow:
		bot = ["Hello !","hi","hi there","welcome"]
		z = random.choice(bot)
		print( 'Bot said - '+z + '\n')
		speak(z)

	elif a.lower() in bye:
		bot = ["sad to see you go :(","bye","miss you"]
		z = random.choice(bot)
		print( 'Bot said - '+z + '\n')
		speak(z)

	elif a.lower() in howare:
		bot = ["I am fine ,thanks ","Happy","I am good"]
		z = random.choice(bot)
		print( 'Bot said - '+z + '\n')
		speak(z)

	elif a.lower() in name:
		bot = ["My name is META bot","You can call me META bot","META Bot in your service","My friends call me META Bot"]
		z = random.choice(bot)
		print( 'Bot said - '+z + '\n')
		speak(z)

	elif a.lower() in bye:
		bot = ["Sad to see you go :(", "Talk to you later", "Goodbye!","Have a nice Day"]
		z = random.choice(bot)
		print( 'Bot said - '+z + '\n')
		speak(z)

	elif a.lower() in menu:
		bot = ["We sell apples!", "Apples are on the menu!","Please take a look at Apples"]
		z = random.choice(bot)
		print( 'Bot said - '+z + '\n')
		speak(z)

	elif a.lower() in hours:
		bot = ["We are open 7am-4pm Monday-Friday!"]
		z = random.choice(bot)
		print( 'Bot said - '+z + '\n')
		speak(z)

	else:
		z= "sorry sir I cannot understand "
		print( 'Bot said - '+z + '\n')
		speak(z)