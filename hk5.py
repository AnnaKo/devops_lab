# !/usr/bin/python
"""python script"""
# pylint: disable=invalid-name

import argparse
import getpass
import requests
# import json

pwd = getpass.getpass(prompt="Enter Your Password: ")

YOURNAME = input("Enter your github user name: ")
YOURREPO = input("Enter the repository name to work with: ")
BRANCHES = "/branches"
PULLS = "/pulls"
COMMITS = "/commits"
RURL = "https://api.github.com/repos/" + YOURNAME + "/" + YOURREPO + PULLS
RURLB = "https://api.github.com/repos/" + YOURNAME + "/" + YOURREPO + BRANCHES
RURLC = "https://api.github.com/repos/" + YOURNAME + "/" + YOURREPO + COMMITS

# RGET = requests.get('https://api.github.com/repos/alenaPy/devops_lab/commits',
# auth=("AnnaKo", pwd))
# RGET = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls', auth=("AnnaKo", pwd))

RGET = requests.get(RURL, auth=("AnnaKo", pwd))
RGETB = requests.get(RURLB, auth=("AnnaKo", pwd))
RGETC = requests.get(RURLC, auth=("AnnaKo", pwd))
JVAR = RGET.json()
JVARB = RGETB.json()
JVARC = RGETC.json()

# JVARC = json.dumps(RGETC.json(), sort_keys = True, indent = 4)
# print(JVARC)

parser = argparse.ArgumentParser(description='AKO ArgParser')
parser.add_argument("-r", "--repo", help="what repository to show", action="store_true")
parser.add_argument("-v", "--version", help="my version is", action="store_true")
parser.add_argument("-n", "--names", help="our names are", action="store_true")
parser.add_argument("-t", "--times", help="creation times", action="store_true")
parser.add_argument("-i", "--repoinfo", help="aggregated repo info", action="store_true")
parser.add_argument("-b", "--branches", help="user branches", action="store_true")
parser.add_argument("-c", "--commits", help="commits and verifications", action="store_true")
akoargs = parser.parse_args()

if akoargs.repo:
    print("Repository Name Is: " + JVAR[0].get("base").get("repo").get("name"))
elif akoargs.version:
    print("This Script Version Is: AKOv1.0")
elif akoargs.names:
    for INDEX in range(30):
        L = JVAR[INDEX].get("head").get("label")
        NAMES, LABELS = L.split(':')
        print("Our Names Are: " + NAMES)
elif akoargs.times:
    for INDEX in range(15):
        L = JVAR[INDEX].get("head").get("repo").get("created_at")
        DATE, TIME = L.split('T')
        print("Time Of Creation Is: " + TIME[0:8:1])
elif akoargs.repoinfo:
    for INDEX in range(10):
        print("RepoInfo:")
        UT = JVAR[INDEX].get("head").get("repo").get("updated_at")
        DATE, TIME = UT.split('T')
        INT = JVAR[INDEX].get("head").get("repo").get("size")
        STR = str(INT)
        URL = JVAR[INDEX].get("head").get("repo").get("url")
        FIRST, LAST = URL.split(YOURREPO)
        print("\tUser: " + FIRST[29::1])
        print("\tLast Update Time: " + TIME[0:8:1])
        print("\tSize: " + STR)
elif akoargs.branches:
    for INDEX in range(5):
        L = JVARB[INDEX].get("name")
        print("List Of Branches: " + L)
elif akoargs.commits:
    for INDEX in range(30):
        print("Commit And Verification:")
        C = JVARC[INDEX].get("commit").get("message")
        V = JVARC[INDEX].get("commit").get("verification").get("verified")
        VS = str(V)
        print("Message Of Commit: " + C)
        print("Verification: " + VS)
else:
    print("Sorry, your parameter is not valid. Please, try another one.")
