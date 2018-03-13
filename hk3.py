# !/usr/bin/python
"""python script"""
# pylint: disable=invalid-name

from datetime import datetime
# from pathlib import Path
import json
import time
import psutil
import config


def METRICS():
    """metrics function"""
    CPU = psutil.cpu_percent()
    OMEM = psutil.swap_memory()
    VMEM = psutil.virtual_memory()
    IO = psutil.disk_io_counters
    NET = psutil.net_if_addrs()
    LIST = [CPU, OMEM, VMEM, IO, NET]
    return str(LIST)


class akoclass():
    """class akoclass"""

    N = 1

    def tojson(self):
        """class function"""
        COUNTER = str(self.N) + ":"
        DICT = {'Snapshot': COUNTER, 'Data': DATE, 'METRICS': METRICS()}
        with open('output.json', 'a') as akojson:
            json.dump(DICT, akojson, indent=4)
        self.N += 1

    def totxt(self):
        """save to text file"""
        COUNTER = "SNAPSHOT" + str(self.N)
        PARAMS = str(COUNTER) + ":" + DATE + ":" + METRICS() + "\n\n"
        file = open("output.txt", "a")
        file.write(PARAMS)
        file.close()
        self.N += 1


cl = akoclass()
"""ako class"""

if config.output == "txt":
    file = open("output.txt", "w")
    file.close()
else:
    file = open("output.json", "w")
    file.close()

while True:
    print(config.interval)
    DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if config.output == "txt":
        cl.totxt()
    else:
        cl.tojson()
    time.sleep(config.interval*60)
