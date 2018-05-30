#!/usr/bin/env python3

#importing speech recognition module 
import speech_recognition as sr

#importing gTTS library from gtts module for text_to_speech
from gtts import gTTS

import subprocess

#importing web browser module for searching in browser
import webbrowser

#starting try block for further error handeling
#try:
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
try:
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
#			if any(i=='make' and i=='directory' for i in user_input):
#				subprocess.getoutput('mkdir /home/Desktop/')		
	
		if any(i=='go' or i=='leave' for i in user_input ):
			end='Have a good day'
			tts(end)
			break
	
		elif any(i=='make' for i in user_input) and any(j=='directory' or j=='directories' for j in user_input):
			#introducing user_defined module	
			import bot_dir as bot
			count_speech='Exactly how many directories you want to introduce ?'
			tts(count_speech)
			dir_count=int(speech_recog())
			print(dir_count)
			if dir_count==1:
				make_speech='From which name you want to introduce directory ?'		
				tts(make_speech)
				dir_name=speech_recog()
				status=bot.bot_mkdir(dir_name,dir_count)				

			else:
					ask_speech='You want to name directories or you want me to name them ?'
					tts(ask_speech)
					user_choice=speech_recog()
					print(user_choice.split())
					if any(i=='I' for i in user_choice.split()) and any(i=="will" for i in user_choice.split()):
						make_speech='Tell me the names by which you want to introduce directories ?'
						tts(make_speech)
						for i in range(dir_count):
							dir_name=speech_recog()
							status=bot.bot_mkdir(dir_name,1)
							tts(status)
					else:
						make_speech='Alright i will name them but tell me the specific name'                          						
						tts(make_speech)
						dir_name=speech_recog()
						status=bot.bot_mkdir(dir_name,dir_count)										
						tts(status)			

		elif any(i==0 for i in c)==False or any(j=='search' for j in user_input):
			
#			for user_input[k] in range(len(user_input))
			for k in range(len(user_input)):
				if user_input[k]=='search':
					search_list=user_input[k+1:len(user_input)]	
					print(search_list)
					search_str=" ".join(search_list)
					webbrowser.open_new_tab('https://www.google.com/search?q='+search_str)
			else:
				webbrowser.open_new_tab('https://www.google.com/search?q='+out_sr)
						
#			inc_task='My freind please assign me some relevant task'
#			tts(inc_task)		
	
		elif any(i=='listen' or i=='play' for i in user_input ):
			import glob
					


except sr.UnknownValueError:
	error='Please check your connectivity'
	tts(error)











