#!/usr/bin/env python3

import serial
import json
import time
import os

imus_activated = False
imus_calibrated = False
encode_done = False

ser = serial.Serial('/dev/ttyS1', 115200)

print("Starting SafeEye, please wait... ")

while not imus_calibrated:
	try:
		line = ser.readline()
		j = ""

		if (encode_done == False):
			print("Init IMUs")
			print("Init calibration (takes 20 secs)")
			time.sleep(10)
			ser.write('imuup'.encode())
			time.sleep(10)
			encode_done = True

		j = json.loads(line.decode())

		if j['type'] == 'status' and not imus_calibrated:

			if j['imusup'] == True and not imus_activated:
				imus_activated = True
				ser.write('calibrate'.encode())

			if j['calibrated'] == True:
				imus_calibrated = True
				ser.close()
				print ("Calibrated")

	except Exception as e:
		print("Init IMUs failed... Retrying...")
		encode_done = False
		continue
