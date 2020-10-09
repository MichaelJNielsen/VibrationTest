import json
from json_setup import telemetry
import random
import signal
import time
import psutil

dict_telemetry = telemetry
filename = "writefile"

def keyboardInterruptHandler(signal,frame):
    print("interrupted")
    with open(filename + ".json", "w") as write_file:
        json.dump(dict_telemetry, write_file, indent=4)
    print(psutil.virtual_memory().percent)
    print(psutil.cpu_percent())
    exit(0)

signal.signal(signal.SIGINT,keyboardInterruptHandler)

i = 0

while True:
    try:
        time.sleep(0.01)
        i = i+1
        dict_telemetry["vicon"]["header"]["sequence"].append(i)
        dict_telemetry["vicon"]["header"]["time stamp"].append(i*10000)
        dict_telemetry["vicon"]["translation"]["x"].append(random.random())
        dict_telemetry["vicon"]["translation"]["y"].append(random.random())
        dict_telemetry["vicon"]["translation"]["z"].append(random.random())
        dict_telemetry["vicon"]["rotation"]["x"].append(random.random())
        dict_telemetry["vicon"]["rotation"]["y"].append(random.random())
        dict_telemetry["vicon"]["rotation"]["z"].append(random.random())
        print(psutil.virtual_memory().percent)
    except Exception as e:
        print("exiting")
        exit(0)
    
    
    
