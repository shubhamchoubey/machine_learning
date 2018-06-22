#!/usr/bin/python3

import cv2
import pytesseract as pytes
import itertools 
#from PIL import Image

cap=cv2.VideoCapture(0)

img1=cap.read()[1]
img2=cap.read()[1]
img3=cap.read()[1]

btg1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
btg2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
btg3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)

while cap.isOpened():
			
	diff1=cv2.absdiff(btg1,btg2)
	diff2=cv2.absdiff(btg2,btg3)
	diff3=cv2.absdiff(diff1,diff2)

	size=diff3.size
	precise=int(0.90*size)
	list_conv=diff3.tolist()
	a=list(itertools.chain(*list_conv))
#		print(a.count(0))
#		print(precise)
	count=0
	for i in a:
		if i<=7:
			count+=1 
	#	print(count)
	#	print(precise)


	if count>=precise:	
		
		text = pytes.image_to_string(btg3,lang='eng')
		print(text)
		if len(text) >= 2:	
			break
			

	status,frame=cap.read()
	btg1=btg2	
	btg2=btg3
	btg3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			
	cv2.imshow('img',frame)


	#img1 = Image.open("sis.jpg")
	

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cap.release()
cv2.destroyAllWindows

