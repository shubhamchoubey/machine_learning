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
		print(out_sr)
		a=[]
		b=[]

		# to run a command	
		for i in user_input:
			output=subprocess.getstatusoutput(i)			
			if output[0]==0 and any(i=="run" for i in user_input) and any(i=='search' for i in user_input):
				
				speech='My freind {0} is {1}'.format(i,output[1])
				tts(speech)
				#storing exit code of a word having exit code 0
				b=b+[output[0]]
		
			else:
					#storing exit code of each word whose exit code does not equal to 0 
				a=a+[output[0]]
			#storing the exit codes of each word present in string 
		c=a+b
	#		if any(i=='make' and i=='directory' for i in user_input):
	#			subprocess.getoutput('mkdir /home/Desktop/')		
		# to close the bot 
		if any(i=='go' or i=='leave' for i in user_input ):
			end='Have a good day'
			tts(end)
			break
		
		# to manage directories
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
					if any(i=='I' for i in user_choice.split()) and any(i=="will" or i=="want" for i in user_choice.split()) and any(i=='don\'t' for i in user_choice.split())==False:
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
						status=bot.bot_mkdir	(dir_name,dir_count)										
						tts(status)			

		# to play songs	at gaana.com	
		elif any(user_input[i]=='play'  or user_input[i]=='listen' for i in range(len(user_input))) and any(user_input[i]=='song' for i in range(len(user_input))):
#			print('hello')
			ind=user_input.index('song')
#			print(ind)
			song_list=user_input[ind+1:]
			song_str=" ".join(song_list)
#			print(song_str)
			#importing userdefined module for video management
			import songs 
			status=songs.songs_play(song_str)
			

		# to play youtube videos 	
		elif any(user_input[i]=='play' or user_input[i]=='watch' or user_input[i]=='see' for i in range(len(user_input))) and any(user_input[i]=='video' for i in range(len(user_input))):
			
			ind=user_input.index('of')

			vid_list=user_input[ind+1:]
			vid_str=" ".join(vid_list)
			print(vid_str)
			#importing userdefined module for video management
			import video as vid
			vid.video_play(vid_str)
		# to send mail from your gmail account
		elif any(i=='send' for i in user_input) and any(i=='mail' for i in user_input):
			recv_id_text='Please tell me the receiver address'
			tts(recv_id_text)
			recv_id_str=speech_recog().split()
			recv_id="".join(recv_id_str)
			print(recv_id)
			sub_text="What subject do you want to attach ?"
			tts(sub_text)
			subject=speech_recog()
			mail_text="What message should i send ?"
			tts(mail_text)
			body=speech_recog()
			import mail_access as ma0
			process=ma.send_mail(recv_id,subject,body)
			tts(process)
	
		elif any(i=='monitor' or i=='surveillance' for i in user_input ):
			import cv2
			import itertools
			cap=cv2.VideoCapture(0)
		
			img1=cap.read()[1]
			img2=cap.read()[1]
			img3=cap.read()[1]
			
			#img6=cap.read()[1]
			btg1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
			btg2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
			btg3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
			#btg6=cv2.cvtColor(img6,cv2.COLOR_BGR2GRAY)
			width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
			height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
			video_format=cv2.VideoWriter_fourcc(*'XVID')
			video_output=cv2.VideoWriter('warning.avi',video_format,25.0,(int(width),int(height)))
			while True:
			
				diff1=cv2.absdiff(btg1,btg2)
				diff2=cv2.absdiff(btg2,btg3)
				diff3=cv2.absdiff(diff1,diff2)
													
				status,frame=cap.read()
	#			sub1=cv2.subtract(x,y)
				size=diff3.size
				precise=int(0.99*size)
				list_conv=diff3.tolist()
				a=list(itertools.chain(*list_conv))
		#		print(a.count(0))
		#		print(precise)
				count=0
				for i in a:
					if i<=10:
						count+=1 
			#	print(count)
			#	print(size)
				if count<=precise:
			#		tts('warning, security breached')
					print('warning')
					video_output.write(frame)
					
			#		print('warning')
#			print(diff3)	

				
				#cv2.imshow('original',frame)
		
				btg1=btg2	
				btg2=btg3
				btg3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
				if cv2.waitKey(1) & 0xFF==ord('q'):
					break 
	
			

			cap.release()
			cv2.destroyAllWindows()
				

		# to search something on google		
		elif any(i==0 for i in c)==False or any(j=='search' for j in user_input):
			try:		
	#			for user_input[k] in range(len(user_input))
				ind=user_input.index('search')
				search_list=user_input[ind+1:]	
				search_str=" ".join(search_list)
				print(search_str)
				webbrowser.open_new_tab('https://www.google.com/search?q={0}'.format(search_str))
			except:
				print(...)
			finally:
				
				webbrowser.open_new_tab('https://www.google.com/search?q='+out_sr)
	#			inc_task='My freind please assign me some relevant task'
	#			tts(inc_task)		
		
				
					
					
except sr.UnknownValueError:
	error='Please check your connectivity'
	tts(error)










