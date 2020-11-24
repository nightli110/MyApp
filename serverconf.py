import os
import sys
import psutil
from collections import OrderedDict
import pprint

def getcpuname():
    CPUinfo=OrderedDict()
    procinfo=OrderedDict()

    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                CPUinfo['proc%s' % nprocs] = procinfo
                nprocs=nprocs+1
                procinfo=OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''

    return CPUinfo['proc0']['model name']

def watchserver(conf):
    serverconf={}
    print ("let me look look your computer")
    serverconf['cpu_name']= getcpuname()
    serverconf['cpu_physical_core']= psutil.cpu_count(logical=False)
    serverconf['cpu_logical_core']= psutil.cpu_count(logical=True)
    serverconf['cpu_freq']= serverconf['cpu_name'].split(' ')[-1]
    serverconf['mem_total']= psutil.virtual_memory().total
    serverconf['disk_total']= psutil.disk_usage('/').total
    #TODO 支持GPU
    # if conf['gpu']:
    #     import pycuda
    #     serverconf['gpu_name']=
    return serverconf





if __name__=="__main__":
    conf=1
    t=watchserver(conf)
    for name in t:
        print(name)
        print(t[name])