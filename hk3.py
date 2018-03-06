#!/usr/bin/python

#pip install psutil
#pip install --upgrade psutil

import psutil
import re
import time
#import json
from datetime import datetime
from pathlib import Path
import config

TFILE = Path("/root/output.txt")
#JFILE = Path("/root/output.json")
DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def METRICS():
  CPU = psutil.cpu_percent()
  OMEM = psutil.swap_memory()
  VMEM = psutil.virtual_memory()
  IO = psutil.disk_io_counters
  NET = psutil.net_if_addrs()
  LIST = [CPU, OMEM, VMEM, IO, NET]
  return str(LIST)

class akoclass():

  def tojson(self):
    #N = 1
    #while True:
      COUNTER = "SNAPSHOT" #+ str(N) + ":"
      DICT = {'Snapshot': COUNTER, 'Data': DATE, 'OMEM': psutil.swap_memory()}
      import json
      with open('output.json', 'a') as akojson:
        json.dump(DICT, akojson)
      #N += 1
      time.sleep(config.interval)
      #akojson.close
  
  def totxt(self):
    N = 1
    if TFILE.exists():
      COUNTER = "SNAPSHOT" + str(N)
      PARAMS = str(COUNTER) + ":" + DATE + ":" + METRICS()
      file = open("output.txt","a") 
      file.write(PARAMS)
      file.close()
      N += 1
      time.sleep(config.interval)
    else:
      COUNTER = "SNAPSHOT" + str(N)
      file = open("output.txt","w")
      PARAMS = str(COUNTER) + ":" + DATE + ":" + METRICS()
      file.write(PARAMS)
      file.close()
      N += 1
      time.sleep(config.interval)

cl = akoclass()
   
if config.output == "txt":
  cl.totxt()
else:
  cl.tojson()






  
