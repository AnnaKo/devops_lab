#!/usr/bin/python

# sudo yum -y install python-nose python3-nose
# pip install PyYAML

import sys
import os
import pip
import json
import site
import yaml

SV = sys.version
VE3 = sys.exec_prefix
VE31, VE32 = VE3.split('versions/')
PEL = sys.executable
PIPL = str(pip.__path__)
PYPATH = os.environ['PATH']
IPACK = sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])
SPL = str(site.getsitepackages())

# print("1 - Python Version is: ",SV[0:5:1])
# print("3 - Python Virtual Environment Is: ", VE32)
# print("4 - Python Executable Location Is: ", PEL)
# print("5 - Pip Location Is: ", PIPL[2:len(PIPL)-2:1])
# print("6 - PYTHONPATH Is: ",PYPATH)
# print("7 - Installed Packages Are: ", ('\n'.join(IPACK)))
# print("8 - Site-Packages Location Is: ", SPL[2:len(SPL)-2:1])

AKODICT = {'1 - Python Version is: ':SV[0:5:1], '3 - Python Virtual Environment Is: ':VE32, '4 - Python Executable Location Is: ':PEL, '5 - Pip Location Is: ':PIPL[2:len(PIPL)-2:1], '6 - PYTHONPATH Is: ':PYPATH, '7 - Installed Packages Are: ':(' '.join(IPACK)), '8 - Site-Packages Location Is: ':SPL[2:len(SPL)-2:1]}

def ako_json():
    with open('json.json', 'a') as ajson:
        json.dump(AKODICT, ajson, indent = 4, ensure_ascii = False)
    #ajson.write()
    ajson.close()
    return 1

def ako_yaml():
    with open('yml.yml', 'a') as ayml:
        yaml.dump(AKODICT, ayml, default_flow_style=False)
    ayml.close()
    return 1

if __name__ == "__main__":
    # execute only if run as a script
    ako_json()
    ako_yaml()
