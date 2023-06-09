#!/usr/bin/python3
import re
from bs4 import BeautifulSoup

# open downloaded HTML file
file = open("test.txt", "r+")
# pass html file into beautiful soup, parse with html.parser
soup = BeautifulSoup(file, "html.parser")

# grabs id name of all task divs
taskList = [item["id"] for item in soup.find_all("div", id=re.compile("^task-num-"))]
# iterates through id names and grabs entire html block, then parses values inside it
for item in taskList:
    task = soup.find("div", {"id": item})
    prototype = task.find("li")
    # For Future: prototype = find[...].text and then try/exception if it doesnt work?
    prototype = prototype.find("code")
    # Cringe work around to find the final item in the list (the filename)
    fileName = task.find("div", {"class": "list-group-item"})
    fileName = fileName.findAll("li")
    fileName = fileName[-1].text[6:]
    f = open(fileName, "w")
    f.write(
        f"#!/usr/bin/python3\n{prototype if prototype else '# Failed to grab prototype, UmU sorry'}\n"
    )
    f.close()

# Terminal Parser

# row = soup.find(string=re.compile('guillaume@ubuntu'))
# # divides terminal example into newlines. Need to parse 'cat main' out of it, find filename after cat, and then copy all text after the cat up until
# #the next terminal prompt
# row.split('\n')
# index = row.find('-main')
# print (index)
# print (row[index])


## Get stuff that doesnt work

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
