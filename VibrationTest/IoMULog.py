import serial
import json
import time

imus_activated = False
imus_calibrated = False

filename = input ("Enter log file name: ")

fout = open (filename,"w")

ser = serial.Serial('/dev/ttyS1',115200)
print("Init IMUs")
ser.write('imuup'.encode())




time.sleep(5)

while True:
	line = ser.readline()
	j = ""
	try: 
		j = json.loads(line.decode())
		if j['type'] == 'telemetry' or j['type'] == 'fft' and imus_activated and imus_calibrated:
			print (j)
			fout.write(str(j)+"\n")
		if j['type'] == 'status' and not imus_calibrated:
			if j['imusup'] == True and not imus_activated:
				print ("Imus up")
				imus_activated = True
				print("Init calibration (takes 10 secs)")
				ser.write('calibrate'.encode())
			if j['calibrated'] == True:
				imus_calibrated = True
				print ("Calibrated")
			#print(j)
	except Exception as e:
		continue