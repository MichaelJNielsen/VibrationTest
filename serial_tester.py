import serial
ser = serial.Serial('/dev/ttyACM0',115200)
#ser = serial.Serial('/dev/ttyS2',115200)

while(True):
    temp = ser.readline() # Read data
    line = temp.decode() # Decode data
    x = line.split() # Comma seperate the data

    print(x)
