#!/usr/bin/python3

import cv2
import pytesseract as pytes
import itertools 
#from PIL import Image

cap=cv2.VideoCapture(0)

img1=cap.read()[1]
img2=cap.read()[1]
img3=cap.read()[1]
#img4=cap.read()[1]
#img5=cap.read()[1]

btg1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
btg2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
btg3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
#btg4=cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
#btg5=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)

while cap.isOpened():
			
	diff1=cv2.absdiff(btg1,btg2)
	diff2=cv2.absdiff(btg2,btg3)
	diff3=cv2.absdiff(diff1,diff2)
#	diff4=cv2.absdiff(btg3,btg4)
#	diff5=cv2.absdiff(btg4,btg5)
#	diff6=cv2.absdiff(diff4,diff5)
#	diff7=cv2.absdiff(diff3,diff6)
#	print(diff3)
	size=diff3.size
	precise=int(0.90*size)
	list_conv=diff3.tolist()
	a=list(itertools.chain(*list_conv))
#	print(a)

	count=0
	for i in a:
		if i<=7:
			count+=1 
	#	print(count)
	#	print(precise)


	if count>=precise:	
		
		text1 = pytes.image_to_string(btg3,lang='eng')
		text2 = pytes.image_to_string(btg2,lang='eng')		
		text3 = pytes.image_to_string(btg1,lang='eng')
		#text4 = pytes.image_to_string(btg2,lang='eng')
		#text5 = pytes.image_to_string(btg1,lang='eng')
		
		count1=0
		count2=0
		count3=0
		#count4=0
		#count5=0
		for i in text1:
			if ord(i) in range(65,91) or ord(i) in range(33,48) or ord(i) in range(58,65):
				count1+=1
		for i in text2:
			if ord(i) in range(65,91) or ord(i) in range(33,48) or ord(i) in range(58,65):
				count2+=1
		for i in text3:
			if ord(i) in range(65,91) or ord(i) in range(33,48) or ord(i) in range(58,65):
				count3+=1
		'''
		for i in text4:
			if ord(i) in range(65,91) or ord(i) in range(33,48) or ord(i) in range(58,65):
				count4+=1
		for i in text5:
			if ord(i) in range(65,91) or ord(i) in range(33,48) or ord(i) in range(58,65):
				count5+=1
		'''
		a=min(count1,count2,count3)
			
			
		#print(a)
		if  a!=0:
			if a is count1:
				print(text1)
				break
			elif a is count2:
				print(text2)
				break
			elif a is count3:
				print(text3)
				break
			#elif a is count4:
			#	print(text4)
			#	break
			#elif a is count5:
			#	print(text5)
			#	break
		#else:
		#	continue			

	status,frame=cap.read()
	btg1=btg2	
	btg2=btg3
#	btg3=btg4
#	btg4=btg5	
	btg3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			
	cv2.imshow('img',frame)


	#img1 = Image.open("sis.jpg")
	

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cap.release()
cv2.destroyAllWindows

