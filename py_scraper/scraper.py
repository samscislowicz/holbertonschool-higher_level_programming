#!/usr/bin/python3
from bs4 import BeautifulSoup
import sys
import subprocess

def check_git():
    try:
        f = open('.git/config', 'r')
    except:
        print(".git/config not found. Start from your repo!")
        exit()
        if ("holbertonschool-higher_level_programming.git" not in f.read()):
            print("Incorrect git repo! Exiting.")
            exit()

def get_fullname():
    flag = 0
    i = 0
    fullnames = []
    for string in soup.strings:
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
    full = get_fullname()
    for string in full:
        print(string)

def print_name():
    flag = 0
    for string in soup.strings:
        if (string == "File: "):
            flag = 1
        elif (flag == 1):
            print(string)
            flag = 0

def get_directories():
    flag = 0
    directories = []
    for string in soup.strings:
        if (string == "Directory: "):
            flag = 1
        elif (flag == 1):
            if (string not in directories):
                directories.append(string)
            flag = 0
    return directories

def print_directories():
    dirs = get_directories()
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
    dirs = get_directories()
    for each in dirs:
        subprocess.call(["mkdir", each])
    fullname = get_fullname()
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

def usage_error():
    print("usage: {} projectnumber operation".format(sys.argv[0]))
    print("Possible operations: ")
    print("name - prints all filenames.")
    print("fullname - prints all filenames and the corresponding directory.")
    print("directories - gives a list of all directories used for the project.")
    print("touch - creates a folder (if needed) for each file, and creates a blank file for each.")
    print("python - finds any linked Github python files and creates them")
    exit()

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
error_soup()
tasks = soup.find_all(attrs={"tasks" : True})

#pythonsource()

#for link in soup:
#    print(link)

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
else:
    usage_error()
#print_all()
