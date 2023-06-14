#!/usr/bin/python3
import re
import sys
from bs4 import BeautifulSoup
from os import chmod


# For Future: prototype = find[...].text and then try/exception if it doesnt work?
def protoParse(task):
    prototype = task.find("li")
    prototype = prototype.find("code")
    return prototype.text if prototype else None


def fileParse(task):
    fileName = task.find("div", {"class": "list-group-item"})
    fileName = fileName.findAll("li")
    fileName = fileName[-1].text
    end = fileName.find(",")
    fileName = fileName[6:end]
    print(fileName)
    return fileName


def mainNameParse(terminal):
    if terminal:
        terminal = terminal.split("\n")
        terminal[0] = terminal[0].split(" ")
        try:
            mainName = terminal[0][2]
        except IndexError:
            print("Possible task without main detected uwu")
        try:
            return mainName
        except UnboundLocalError:
            return


def mainContentParse(terminal):
    if terminal:
        terminal = terminal.split("\n")
        counter = 0
        content = []
        for index, value in enumerate(terminal):
            found = value.find(":~/$")
            if found != -1:
                counter += 1
            if counter == 1:
                end = index
        if counter == 0:
            return None
        for i in range(1, end):
            content.append(terminal[i])
        return content


def createMain(content, mainName):
    if mainName:
        main = open(mainName, "w")
        chmod(mainName, 777)
        for i in content:
            main.write(i + "\n")
        main.close


def createFile(prototype, fileName):
    f = open(fileName, "w")
    chmod(fileName, 777)
    f.write(
        f"#!/usr/bin/python3\n{prototype if prototype else '# Failed to grab prototype, UmU sorry'}\n"
    )
    f.close()


# open downloaded HTML file
try:
    file = open("test.txt", "r+")
except FileNotFoundError:
    print("test.txt not found :<")
    sys.exit(1)
# pass html file into beautiful soup, parse with html.parser
soup = BeautifulSoup(file, "html.parser")
file.close()

# grabs id name of all task divs
taskList = [item["id"]
            for item in soup.find_all("div", id=re.compile("^task-num-"))]
# iterates through id names and grabs entire html block, then parses values inside it
for item in taskList:
    task = soup.find("div", {"id": item})
    prototype = protoParse(task)
    fileName = fileParse(task)
    terminal = task.find(string=re.compile("guillaume@ubuntu"))
    mainName = mainNameParse(terminal)
    content = mainContentParse(terminal)
    createMain(content, mainName)
    createFile(prototype, fileName)

# Get stuff that doesnt work

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
