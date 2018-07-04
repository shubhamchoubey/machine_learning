#!/usr/bin/python3

def survillence():
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
	var=[]
	var1=[]
	while True:
			
		diff1=cv2.absdiff(btg1,btg2)
		diff2=cv2.absdiff(btg2,btg3)
		diff3=cv2.absdiff(diff1,diff2)
													
		status,frame=cap.read()
	#			sub1=cv2.subtract(x,y)
		size=diff3.size
		precise=int(0.90*size)
		list_conv=diff3.tolist()
		a=list(itertools.chain(*list_conv))
		#		print(a.count(0))
		#		print(precise)
		count=0
		for i in a:
			if i<=8:
				count+=1 
			#	print(count)
			#	print(precise)
		
		a=0
		if count<=precise:
			
			var=var+[0]
			video_output.write(frame)
			#		tts('warning, security breached')
		#	r		subprocess.getoutput('mpg321 text.mp3')
			#	print('warning')
		#	z=z+var
		
		elif len(var)>5:
			var1=var1+[1]
		print(var)
		print(var1)
		for i in var1:
			a+=i
			if a==25:
				return 'warning'	
		#			print('warning')
#			print(diff3)	

				
		#cv2.imshow('original',frame)
		
		btg1=btg2	
		btg2=btg3
		btg3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		if 0xFF==ord('q'):
			break 
	
			

	cap.release()
	cv2.destroyAllWindows()
				








