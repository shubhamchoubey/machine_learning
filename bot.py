#!/usr/bin/env python3

#importing speech recognition module 
import speech_recognition as sr

#importing gTTS library from gtts module for text_to_speech
from gtts import gTTS

import subprocess

#importing web browser module for searching in browser
import webbrowser

#starting try block for further error handeling
try:
	#defining function for text to speech conversion
	def tts(text):
		tts=gTTS(text,lang='en')
		tts.save('text.mp3')
		subprocess.getoutput('mpg321 text.mp3')

	def speech_recog():
		#loading class recognizer
		recog=sr.Recognizer()
		with sr.Microphone() as source:
			audio=recog.listen(source)
		#storing input in a variable
		speech_string=recog.recognize_google(audio).strip()
		return speech_string

	wlcome_text="Hello i am a bot, how can i help you ?"
	tts(wlcome_text)

	while True:
		out_sr=speech_recog()
		user_input=out_sr.split()
		print(user_input)
		a=[]
		b=[]
		for i in user_input:
			output=subprocess.getstatusoutput(i)
			if output[0]==0 and any(i=="search" for i in user_input)==False :
				speech='My freind {0} is {1}'.format(i,output[1])
				tts(speech)
				#storing exit code of a word having exit code 0
				b=b+[output[0]]
	
			else:
				#storing exit code of each word whose exit code does not equal to 0 
				a=a+[output[0]]
		#storing the exit codes of each word present in string 
		c=a+b
		if any(i=='go' or i=='leave' for i in user_input ):
			end='Have a good day'
			tts(end)
			break

		elif any(i==0 for i in c)==False or any(j=='search' for j in user_input):
			webbrowser.open_new_tab('https://www.google.com/search?q='+out_sr)

			
#			inc_task='My freind please assign me some relevant task'
#			tts(inc_task)		

except sr.UnknownValueError:
	error='Please check your connectivity'
	tts(error)





