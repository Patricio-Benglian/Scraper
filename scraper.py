#!/usr/bin/python3
import re
from bs4 import BeautifulSoup

# open downloaded HTML file
file = open("test.txt", "r+")
# pass html file into beautiful soup, parse with html.parser
soup = BeautifulSoup(file, 'html.parser')

# Working
row = soup.find_all(string=('Prototype: '))
for r in row:
    nextSib = r.nextSibling
    print(nextSib.text)

print('~~~~~~~~~~~~~~~~~~~')

# Working  
row = soup.find_all(string=('File: '))
for r in row:
    nextSib = r.nextSibling
    print(nextSib.text)

print("~~~~~~~~~~~~~~~~~~~")

row = soup.find(string=re.compile('guillaume@ubuntu'))
# divides terminal example into newlines. Need to parse 'cat main' out of it, find filename after cat, and then copy all text after the cat up until
#the next terminal prompt
row.split('\n')
index = row.find('-main')
print (index)
print (row[index])



# import requests
# from requests.auth import HTTPBasicAuth
# import requests.auth
# from getpass import getpass


# response = requests.get('https://intranet.hbtn.io/projects/2122', auth=HTTPBasicAuth('X', getpass()))
# f = open("intranet_html.txt", "w")
# f.write(response.text)
# f.close()
# print (response.status_code)

# # Authentication is failing or i am not downloading the correct page