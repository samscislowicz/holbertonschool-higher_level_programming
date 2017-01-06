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

def get_name(task):
    flag = 0
    i = 0
    for string in task.strings:
        if (string == "File: "):
            flag = 1
        elif (flag == 1):
            return(string)

def get_fullname(task):
    flag = 0
    i = 0
    for string in task.strings:
        if (string == "File: "):
            flag = 1
        elif (string == "Directory: "):
            flag = 2
        elif (flag == 1):
            fullname += string
            flag = 0
        elif (flag == 2):
            fullname = (string + "/")
            flag = 0
    return fullname

def print_fullname():
    for project in plist:
         print(project.fullname)

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
    for string in task.strings:
        if (string == "Directory: "):
            flag = 1
        elif (flag == 1):
            return(string)
            flag = 0

def print_directories():
    dirs = []
    for project in plist:
        if project.directory not in dirs:
            print (project.directory)
            dirs.append(project.directory)

def pythonsource(project):
    for a in project.task.find_all("a", string="here"):
        newline = a["href"]
        newline = "https://raw.githubusercontent.com/" + newline[19:]
        start = newline.rfind('/blob/')
        newline = newline[:start] + newline[start + 5:]
        source = requests.get(newline)
        newfile = open(project.fullname, 'w')
        newfile.write(source.text)
        return (True)
    return (None)

def touch():
    for project in plist:
        if (os.path.isdir(project.directory) != True):
            subprocess.call(["mkdir", project.directory])
        subprocess.call(["touch", project.fullname])
        template = get_template(project)
        if (template != None):
            file = open(project.fullname, "w")
            file.write(open(template, "r").read())
        open(project.directory + "/README.md", "a").write(project.name + '\n')
        pythonsource(project)
        make_mains()

def get_template(project):
    if (re.search(".py$", project.name) != None):
        return("templates/python.template")
    if (re.search(".c$", project.name) != None):
        return("templates/c.template")
    if (re.search(".sh$", project.name) != None):
        return("templates/bash.template")
    return(None)

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
    print("all - prints the whole HTML result from the project page (prettified)")
    exit()

def get_extra():
    for task in tasks:
        print(get_extra(task))

def make_mains():
    for task in tasks:
        for string in task.strings:
            result = re.search('cat(.)*main.py', string)
            if (result != None):
                filename = string[result.start(0) + 4:result.end(0)]
                if (filename != None):
                    direct = get_directories(task)
                    filename = direct + "/" + filename
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

class Project:
    def __init__(self, task):
        self.name = get_name(task)
        self.fullname = get_fullname(task)
        self.directory = get_directories(task)
        self.number = get_project_number(task)
        self.task = task
        self.type = "python"
#       self.repository
#       self.extra (mains inside project)

def project_list():
    projectlist = [ Project(task) for task in tasks ]
    return projectlist

plist = project_list()
#for project in plist:
#    print(project.number)
#    print(project.name)
#    print(project.fullname)
#    print(project.directory)
#    print('\n')
#exit()

for project in plist:
        get_template(project)
          
error_soup()
if (sys.argv[2] == 'fullname'):
    print_fullname()
elif (sys.argv[2] == 'name'):
    print_name()
elif (sys.argv[2] == 'touch'):
    touch()
elif (sys.argv[2] == 'directories'):
    print_directories()
elif(sys.argv[2] == 'all'):
    print(soup.prettify())
else:
    usage_error()
#print_all()


# TODO:
# Check for files before creating them
# Warn that file exists and is not empty and give option to overwrite?
# Append instead of write by default?
# Figure out best way to handle this.
