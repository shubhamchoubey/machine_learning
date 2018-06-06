import requests
from bs4 import BeautifulSoup
import subprocess
import webbrowser
def songs_play(user_str):
#try:
				
	page=requests.get('https://gaana.com/search/{}'.format(user_str))

	soup=BeautifulSoup(page.text,'html.parser')
		
	artist_name_list = soup.find(class_='BodyText')
	
	items=soup.findAll('a')
	
	for i in items:
		if i.get('href')!=None and i.get('href').count('song')>0 and i.get('href').count('search')==0:
			string=str(i.get('href'))
#			print(string)
			webbrowser.open_new_tab(string)
			break	

		else:
			continue
	
#	except :
#		return('sorry there is some error please try again')


'''
	for i in items.get('href'):
		
			string="https://www.youtube.com"+str(i)
			print(string)
#			subprocess.getoutput('vlc {}'.format(string))
				

'''		
			


