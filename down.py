from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui
from requests import get
from  bs4 import BeautifulSoup
import requests
import csv
import re
# Fiz algumas modificações

         
class AnimeBot:
    def __init__(self):
        # self.arquivo=arquivo
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
        firefox_profile=firefoxProfile, executable_path=r"C:\\geckodriver.exe")
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """

    def baixar(self,arquivo):
        anime=self.driver
        anime.get(arquivo)

        time.sleep(3)
        lapis= anime.find_element_by_partial_link_text('Clique')
        print(lapis)
        lapis.click()
        time.sleep(3)

        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.click(x=480, y=450)
        pyautogui.hotkey('Ctrl','j')
        time.sleep(300)




        '''
        a_element = driver.find_element_by_xpath("//input[@id='input_username']")
        a_element.send_keys(self.a)
        b_element = driver.find_element_by_xpath("//input[@id='input_password']")
        b_element.send_keys(self.b)
        login_button = driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()'''

def busca(url):
        lista=[]
        fonte = requests.get(url).text
        soup = BeautifulSoup(fonte,'lxml')
        for i in soup.find_all(href=re.compile("baixar")):
                nome=i
                links=(i['href'])
                if links not in lista:
                    lista.append(links)
        return(lista)     
              

def interface():
        termina=False
        while termina is False:
            url=str(input("digite a url"))
            print("Buscando episodioss na url:")
            
            episodios=busca(url)
            print(f'Estes são os episodios encontrados:{episodios}')
            
            ep=int(input("Aperte um número para baixar o episodios ou 666 para terminar:"))
            if ep==1:
                arquivo=episodios[1]
            if ep==2:
                arquivo=episodios[2]
            if ep==3:
                arquivo=episodios[3]
            if ep==4:
                arquivo=episodios[4]
            if ep==5:
                arquivo=episodios[5]
                print(arquivo)
            if ep==6:
                arquivo=episodios[6]
            if ep==7:
                arquivo=episodios[7]
            if ep==8:
                arquivo=episodios[8]
            if ep==9:
                arquivo=episodios[9]
            if ep==10:
                arquivo=episodios[10]
            if ep==11:
                arquivo=episodios[11]
            if ep==12:
                arquivo=episodios[12]
            if ep==666:
                termina=True
            
            
            else:
                print('voltando')
            
            Anime = AnimeBot()
            Anime.baixar(arquivo)
		# Anime.baixar(link)
if __name__ == "__main__":
	interface()
        #https://www.meuanime.com/baixar?file=4402063
	# pagina=str(input("Digite a pagina de download do anime:"))
	# ep=int(input("Digite o numero de ep:") )
	# for t in range(ep):
		# link=str(input("Digite o o link:"))
		# Anime = AnimeBot()
		# Anime.baixar(link)
        
        
        
        