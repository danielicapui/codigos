import requests
from bs4 import *
import wget
import shutil
import urllib.request
# url = 'https://www.meuanime.com/baixar?file=12414343'

# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
# result = requests.get(url, headers=headers)
# print(result.content.decode())

def download(url, file_name,headers):
  # open in binary mode
	#response = requests.get(url, headers=headers)
	r =requests.get(url,stream=True, headers={'User-agent': 'Mozilla/5.0'})
	
	if  r.status_code==200:
		with  open(file_name, 'wb') as file:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, file)
			#file.write(response.content)
			print(f'baixando:{file_name}')
		
		

if __name__ == "__main__":
	url = 'https://www.meuanime.com/download.php?file=NWY2OWI4ZDhhMGU1OWQ2ZQ==&token=pSObHtMTU5NzYyMjI4Mw==&n=bGFwaXMtcmUtbGlnaHRzLWVwaXNvZGlvLTY='

	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
	file_name='lapis6.mp4'
	download(url,file_name,headers)