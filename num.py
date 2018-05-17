#!/usr/bin/env python3

import numpy as np
user_data=[]
user_input=[]
#while user_input!=['q'] :
user_input=input('enter data :' ).strip().split(',')
       #	list_conv=[user_data]



print(user_input)
length=len(user_input)
print(length)
a=0
for i in range(2,length):
    if length%i==0:
        a=a+1   
#user_data=user_input[0:length]

if a==0:
	extra_element=[input('Enter one more element: ')]
	user_input = user_input + extra_element

length=len(user_input)
#print(len(user_data))   
	
factor=[]

#print(user_data,length)
for i in range(2,length):
    if length%i==0:
       factor=factor+[i]
           

#print(type(factor))
for i in factor:

#     print(i)
     combination=length/i
#     print(combination)
     print(int(combination),i)

comb_input=(input("which combination you want ?").strip().split(','))

#print(comb_input)
array=np.array(user_input)
conv_inp=()

for i in comb_input:
	conv_inp=conv_inp+(int(i),)
#print(conv_inp)
print(np.reshape(array,conv_inp))

'''
if length%2==0:
   while length/2!=1:
       x=length/2
       print('['+x+',2]')

else:
  user_data= user_data + [input('enter one more number:' )]

'''
