import random

hellow = ["hi","is anyone there?", "hello", "good day","hello there"]
bye = ["hi","cya", "see you later","bye" ,"goodbye", "i am Leaving", "have a Good day"]
howare = ["hi","how are you","whats up","how you doing"]
name = ["hi","whats your name","what is your name","do you have any name","what should i call you","name"]
menu = ["i want to buy something", "what is on the menu", "what do you reccommend?", "could i get something to eat"]
hours = ["when are you guys open", "what are your hours", "hours of operation","time","work time","time period"]

print("*******************************************************\n")

while True:
	a = input('User said -')

	if a.lower() in hellow:
		bot = ["Hello !","hi","hi there","welcome"]
		z = random.choice(bot) 
		print('Bot said - '+ z +'\n')

	elif a.lower() in bye:
		bot = ["sad to see you go :(","bye","miss you"]
		z = random.choice(bot) 
		print('Bot said - '+ z +'\n')

	elif a.lower() in howare:
		bot = ["I am fine ,thanks ","Happy","I am good"]
		z = random.choice(bot) 
		print('Bot said - '+ z +'\n')

	elif a.lower() in name:
		bot = ["My name is TVC bot","You can call me TVC bot","TVC Bot in your service","My friends call me TVC Bot"]
		z = random.choice(bot) 
		print('Bot said - '+ z +'\n')

	elif a.lower() in bye:
		bot = ["Sad to see you go :(", "Talk to you later", "Goodbye!","Have a nice Day"]
		z = random.choice(bot) 
		print('Bot said - '+ z +'\n')

	elif a.lower() in menu:
		bot = ["We sell apples!", "Apples are on the menu!","Please take a look at Apples"]
		z = random.choice(bot) 
		print('Bot said - '+ z +'\n')

	elif a.lower() in hours:
		bot = ["We are open 7am-4pm Monday-Friday!"]
		z = random.choice(bot) 
		print('Bot said - '+ z +'\n')

	else:
		z = Sorry!, I cannot understand
		print('Bot said - '+ z +'\n')