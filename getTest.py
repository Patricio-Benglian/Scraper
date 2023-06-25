#!/usr/bin/python3
"""
Still a WIP and sucks!
"""
import requests

url = "https://intranet.hbtn.io/projects/2182"
cookies = dict(cookie="")

response = requests.get(url, cookies=cookies)
f = open("intranet_html.txt", "w")
f.write(response.text)
f.close()

# Authentication is failing or i am not downloading the correct page
