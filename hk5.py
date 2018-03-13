# !/usr/bin/python
"""python script"""
# pylint: disable=invalid-name

import argparse
import getpass
import requests
# import json

parser = argparse.ArgumentParser(description='AKO ArgParser')
# parser.add_argument("-r", "--repo", help="what repository to show", action="store_true")
parser.add_argument("-v", "--version", help="my version is", action="store_true")
parser.add_argument("-n", "--names", help="our names are", action="store_true")
parser.add_argument("-t", "--times", help="creation times", action="store_true")
parser.add_argument("-i", "--repoinfo", help="aggregated repo info", action="store_true")
parser.add_argument("-b", "--branches", help="user branches", action="store_true")
parser.add_argument("-c", "--commits", help="commits and verifications", action="store_true")
akoargs = parser.parse_args()

pwd = getpass.getpass(prompt="Enter Your Password: ")

YOURNAME = input("Enter your github user name: ")
YOURREPO = input("Enter the repository name to work with: ")
BRANCHES = "/branches"
PULLS = "/pulls"
COMMITS = "/commits"
RURL = "https://api.github.com/repos/" + YOURREPO + PULLS
RURLB = "https://api.github.com/repos/" + YOURREPO + BRANCHES
RURLC = "https://api.github.com/repos/" + YOURREPO + COMMITS

# RGET = requests.get('https://api.github.com/repos/alenaPy/devops_lab/commits',
# auth=("AnnaKo", pwd))
# RGET = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls', auth=("AnnaKo", pwd))

RGET = requests.get(RURL, auth=(YOURNAME, pwd))
RGETB = requests.get(RURLB, auth=(YOURNAME, pwd))
RGETC = requests.get(RURLC, auth=(YOURNAME, pwd))
JVAR = RGET.json()
JVARB = RGETB.json()
JVARC = RGETC.json()

# JVARC = json.dumps(RGETC.json(), sort_keys = True, indent = 4)
# print(JVARC)

# if akoargs.repo:
    # for INDEX in JVAR:
        # L = INDEX.get("base").get("repo").get("name")
        # JVAR[0].get("base").get("repo").get("name")
        # print("Repository Name Is: " + L)
if akoargs.version:
    print("This Script Version Is: AKOv1.0")
elif akoargs.names:
    for INDEX in JVAR:
        L = INDEX.get("head").get("label")
        NAMES, LABELS = L.split(':')
        print("Our Names Are: " + NAMES)
elif akoargs.times:
    for INDEX in JVAR:
        L = INDEX.get("head").get("repo").get("created_at")
        DATE, TIME = L.split('T')
        print("Time Of Creation Is: " + TIME[0:8:1])
elif akoargs.repoinfo:
    for INDEX in JVAR:
        print("RepoInfo:")
        UT = INDEX.get("head").get("repo").get("updated_at")
        DATE, TIME = UT.split('T')
        INT = INDEX.get("head").get("repo").get("size")
        STR = str(INT)
        # URL = INDEX.get("head").get("repo").get("url")
        # FIRST, LAST = URL.split(PULLS)
        print("\tRepository Full Name: " + YOURREPO)
        print("\tLast Update Time: " + TIME[0:8:1])
        print("\tSize: " + STR)
elif akoargs.branches:
    for INDEX in JVARB:
        L = INDEX.get("name")
        print("List Of Branches: " + L)
elif akoargs.commits:
    for INDEX in JVARC:
        print("Commit And Verification:")
        C = INDEX.get("commit").get("message")
        V = INDEX.get("commit").get("verification").get("verified")
        VS = str(V)
        print("Message Of Commit: " + C)
        print("Verification: " + VS)
else:
    print("Sorry, your parameter is not valid. Please, try another one.")
