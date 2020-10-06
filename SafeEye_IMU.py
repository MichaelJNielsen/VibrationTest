#!/usr/bin/env python2
import serial, json
from json_setup import telemetry
dict_telemetry = telemetry
ser = serial.Serial('/dev/ttyS1',115200)
filename = "temp/Telemetry.json"

def telemetry_json():
    while True:
        read_from_safeeye()
        with open(filename, 'w') as f:
            json.dump(dict_telemetry, f)
    time.sleep(0.1)

def read_from_safeeye():
    line = ser.readline()
    j = ""
    try:
        j = json.loads(line.decode())
        dict_telemetry.update(j)

    except Exception as e:
        print("Error")

if __name__ == '__main__':
    telemetry_json()
