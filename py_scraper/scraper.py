#!/usr/bin/python3
from bs4 import BeautifulSoup
import sys
import subprocess
import re

def check_git():
    try:
        f = open('.git/config', 'r')
    except:
        print(".git/config not found. Start from your repo!")
        exit()
        if ("holbertonschool-higher_level_programming.git" not in f.read()):
            print("Incorrect git repo! Exiting.")
            exit()

def get_fullname(task):
    flag = 0
    i = 0
    fullnames = []
    for string in task.strings:
        if (string == "File: "):
            flag = 1
        elif (string == "Directory: "):
            flag = 2
        elif (flag == 1):
            fullnames[-1] += string
            flag = 0
        elif (flag == 2):
            fullnames.append(string + "/")
            flag = 0
    return fullnames

def print_fullname():
    for task in tasks:
        full = get_fullname(task)
        for string in full:
            print(string)

def print_name():
    flag = 0
    for task in tasks:
        for string in task.strings:
            if (string == "File: "):
                flag = 1
            elif (flag == 1):
                print(string)
                flag = 0

def get_directories(task):
    flag = 0
    directories = []
    for string in task.strings:
        if (string == "Directory: "):
            flag = 1
        elif (flag == 1):
            if (string not in directories):
                directories.append(string)
            flag = 0
    return directories

def print_directories():
    for task in tasks:
        dirs = get_directories(task)
        for string in dirs:
            print(string)

def pythonsource():
    for a in soup.find_all("a", string="here"):
        newline = a["href"]
        newline = "https://raw.githubusercontent.com/" + newline[19:]
        start = newline.rfind('/blob/')
        newline = newline[:start] + newline[start + 5:]
        source = requests.get(newline)
        print(source.text)

def touch():
    for task in tasks:
        dirs = get_directories(task)
        for each in dirs:
            if (os.path.isdir(each) != True):
                subprocess.call(["mkdir", each])
            fullname = get_fullname(task)
            for name in fullname:
                subprocess.call(["touch", name])

def print_all():
    for string in soup.strings:
        print(string)

def error_soup():
    if ("The page you were looking for doesn't exist (404)" in soup.strings):
        print("Incorrect project number, 404 error.")
        exit()
    if ("The project you requested is not available to you yet!" in soup.strings):
        print("Incorrect project number, not available.")
        exit()
    if ('{"success":false,"message":"You need to sign in before."}' in soup.strings):
        print("Incorrect login. Check that your cookies.txt is valid.")
        exit()

def usage_error():
    print("usage: {} projectnumber operation".format(sys.argv[0]))
    print("Possible operations: ")
    print("name - prints all filenames.")
    print("fullname - prints all filenames and the corresponding directory.")
    print("directories - gives a list of all directories used for the project.")
    print("touch - creates a folder (if needed) for each file, and creates a blank file for each.")
    print("extra - creates any additional files (such as main files) and fills them in.")
    print("python - finds any linked Github python files and creates them")
    exit()

def make_extra():
    make_mains(direct)
    exit()

def make_mains(direct):
    for string in soup.strings:
        result = re.search('cat(.)*main.py', string)
        if (result != None):
            filename = string[result.start(0) + 4:result.end(0)]
            if (filename != None):
                filename = direct + filename
            user = re.search('(.)*@ubuntu:(.)*', string)
            string = string[user.end(2) + 2:]
            user = re.search('(.)*@ubuntu:(.)*', string)
            string = string[:user.start(0)]
            newfile = open(filename, 'w')
            newfile.write(string)

def get_project_number(task):
    h4 = task.find('h4', class_="task")
    text = h4.text
    period = text.find('.')
    num = int(text[5:period])
    return (num)

if (len(sys.argv) < 3):
    usage_error()

import http.cookiejar, requests
cj = http.cookiejar.MozillaCookieJar()
import os

cookies = os.environ['HOME'] + '/cookies.txt'
try:
    cj.load(cookies)
except FileNotFoundError:
    print("No cookie file found! Please put your cookie file in ~/cookies.txt.")
    exit()

url = 'https://intranet.hbtn.io/projects/'
url += sys.argv[1]

page = requests.get(url, cookies=cj)
soup = BeautifulSoup(page.content, "lxml")
tasks = soup.find_all('div', class_=" clearfix gap")
#tasks = [ ]

#class Project:
#    def __init__(self, task):
#        self.name = get_name(task)
#        self.directory = get_directories(task)
#        self.number = get_project_number(task)


error_soup()
if (sys.argv[2] == 'fullname'):
    print_fullname()
elif (sys.argv[2] == 'name'):
    print_name()
elif (sys.argv[2] == 'touch'):
    touch()
elif (sys.argv[2] == 'directories'):
    print_directories()
elif(sys.argv[2] == 'python'):
    pythonsource()
elif(sys.argv[2] == 'all'):
    print_all()
elif(sys.argv[2] == 'extra'):
    make_extra(None)
elif(sys.argv[2] == 'number'):
    for task in tasks:
        print("{:d}".format(get_project_number(task)))
else:
    usage_error()
#print_all()
