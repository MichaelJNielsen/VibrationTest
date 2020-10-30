import serial, csv, time

ser = serial.Serial('/dev/ttyACM0',115200)
#ser = serial.Serial('/dev/ttyS2',115200)
file_name = "data_serial_tester.csv"
latest_received = '0,0,0,0,0,0,0,0,0,0'
buffer_bytes = b''

def read_latest_line(ser):
        global latest_received, buffer_bytes
        bytesToRead = ser.inWaiting()
        temp_bytes = ser.read(bytesToRead)
        buffer_bytes = buffer_bytes + temp_bytes
        buffer_string = buffer_bytes.decode()
        buffer_bytes = temp_bytes
        lines = buffer_string.split('\r\n')
        if len(lines) > 1:
            latest_received = lines[-2]
        else:
            print("Not enough serial input, using last available")
        return latest_received

def read_from_serial(ser):
    serial_data = []
    line = read_latest_line(ser)
    splitline = line.split(',') # Comma seperate the data
    #print(splitline)
    for x in splitline:
        serial_data.append(float(x))
    return serial_data

while True:
    time.sleep(0.02)
    data = read_from_serial(ser)
    #print(data)
    with open(file_name, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
