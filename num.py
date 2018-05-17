#!/usr/bin/env python3

import numpy as np
user_input=input('enter data :' ).strip().split(',')

#print(user_input)
length=len(user_input)
#print(length)
a=0
for i in range(2,length):
    if length%i==0:
        a=a+1   

if a==0:
	extra_element=[input('Enter one more element: ')]
	user_input = user_input + extra_element

length=len(user_input)  
	
factor=[]

for i in range(2,length):
    if length%i==0:
       factor=factor+[i]
           
for i in factor:
     combination=length/i
     print(int(combination),i)

comb_input=(input("which combination you want ?").strip().split(','))

array=np.array(user_input)
conv_inp=()

for i in comb_input:
	conv_inp=conv_inp+(int(i),)
print(np.reshape(array,conv_inp))
