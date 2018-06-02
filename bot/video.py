import requests
from bs4 import BeautifulSoup
import subprocess

def video_play(user_string):
	
	page=requests.get('https://www.youtube.com/results?search_query={}'.format(user_string))

	soup=BeautifulSoup(page.text,'html.parser')
	#last_links = soup.find(class_='AlphaNav')
	#last_links.decompose()
		
	artist_name_list = soup.find(class_='BodyText')
	
	items=soup.findAll('a')
#	print(type(items))

	for i in items:
		if i.get('href').count('/watch')>0:
			string="https://www.youtube.com"+str(i.get('href'))
#			print(string)
			subprocess.getoutput('vlc {}'.format(string))
			break	
#			video=pafy.new(string)
#			best=video.getbest()
#			print(best)
			
		else:
			continue


'''
artist_name_list_items = artist_name_list.find_all('a')


for artist_name in artist_name_list_items:
    links = artist_name.get('href')
    print(links)

'''
