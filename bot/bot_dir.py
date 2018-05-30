#!/usr/bin/env python3
import subprocess

def bot_mkdir(dir_name,dir_count):
	a=[]
	for i in range(dir_count):
		mkdir=subprocess.getstatusoutput('mkdir {}_{}'.format(dir_name,i))
		a=a+[mkdir[0]]
		
	if all(i==0 for i in a):
		if dir_count==1:
			return 'directory introduced successfully'
		else:
			return 'directordies introduced successfully'

	else:
		return 'there is some problem in the operation please check it'

