#! /usr/bin/env python
import sys, signal, time, rospy, serial, datetime, setup, csv, os
from json_setup import telemetry
from tkinter.filedialog import asksaveasfile
from sensor_msgs.msg import Imu
from sensor_msgs.msg import Joy
from geometry_msgs.msg import TransformStamped

dict_telemetry = telemetry

#ser1 = serial.Serial('/dev/ttyS2',115200)
#ser1 = serial.Serial('/dev/ttyACM0',115200)
ser2 = serial.Serial('/dev/ttyACM0',115200)
latest_received = '0,0,0,0,0,0,0,0,0,0'
buffer_bytes1 = b''
buffer_bytes2 = b''

def keyboardInterruptHandler(signal,frame):
    print("\ninterrupted")
    exit(0)

signal.signal(signal.SIGINT,keyboardInterruptHandler)
            
def log(data1, data2):
        try:
                global start_flag, start_time
                if start_flag == 0:
                        start_time = time.time()
                        field_header = [dict_telemetry["test id"]["name"], dict_telemetry["test id"]["date"]]
                        start_flag = 1
                        
                else:
                        field_header = ['','']
                
                current_clocktime = datetime.datetime.now().time()
                dict_telemetry["test id"]["time"] = float(current_clocktime.strftime("%H%M%S.%f"))
                dict_telemetry["test id"]["time_since_start"] = time.time()-start_time
                
                field_time = [dict_telemetry["test id"]["time"], dict_telemetry["test id"]["time_since_start"]]
                field_vicon = [dict_telemetry["vicon"]["header"]["sequence"],float(str(dict_telemetry["vicon"]["header"]["seconds"]) + "." + str(dict_telemetry["vicon"]["header"]["nanoseconds"])),dict_telemetry["vicon"]["header"]["frame id"], dict_telemetry["vicon"]["child frame id"], dict_telemetry["vicon"]["translation"]["x"], dict_telemetry["vicon"]["translation"]["y"], dict_telemetry["vicon"]["translation"]["z"], dict_telemetry["vicon"]["rotation"]["x"], dict_telemetry["vicon"]["rotation"]["y"], dict_telemetry["vicon"]["rotation"]["z"], dict_telemetry["vicon"]["rotation"]["w"]]
                field_int_imu = [data1[0], data1[1], data1[2], data1[3], data1[4], data1[5], data1[6], data1[7], data1[8], data1[9]]
                field_ext_imu = [data2[0], data2[1], data2[2], data2[3], data2[4], data2[5], data2[6], data2[7], data2[8], data2[9]]
                field_dji_imu = [dict_telemetry["dji imu"]["header"]["sequence"], float(str(dict_telemetry["dji imu"]["header"]["seconds"]) + "." + str(dict_telemetry["dji imu"]["header"]["nanoseconds"])), dict_telemetry["dji imu"]["header"]["frame id"], dict_telemetry["dji imu"]["orientation"]["x"], dict_telemetry["dji imu"]["orientation"]["y"], dict_telemetry["dji imu"]["orientation"]["z"], dict_telemetry["dji imu"]["orientation"]["w"], dict_telemetry["dji imu"]["angular velocity"]["x"], dict_telemetry["dji imu"]["angular velocity"]["y"], dict_telemetry["dji imu"]["angular velocity"]["z"], dict_telemetry["dji imu"]["linear acceleration"]["x"], dict_telemetry["dji imu"]["linear acceleration"]["y"], dict_telemetry["dji imu"]["linear acceleration"]["z"]]
                field_rc = [dict_telemetry["rc"]["header"]["sequence"], float(str(dict_telemetry["rc"]["header"]["seconds"]) + "." + str(dict_telemetry["rc"]["header"]["nanoseconds"])), dict_telemetry["rc"]["header"]["frame id"], dict_telemetry["rc"]["roll"], dict_telemetry["rc"]["pitch"], dict_telemetry["rc"]["yaw"], dict_telemetry["rc"]["throttle"], dict_telemetry["rc"]["mode"], dict_telemetry["rc"]["landing_gear"]]
                fields = field_header + field_time + field_vicon + field_int_imu + field_ext_imu + field_dji_imu + field_rc
                #print(field_ext_imu)
                with open(file_name, 'a', newline='') as f:
                        writer = csv.writer(f) 
                        writer.writerow(fields)
        except Exception as e:
                print("Logging error")

def logsetup():
        try:
                global start_flag
                start_flag = 0
                
                date = datetime.date.today()

                dict_telemetry["test id"]["name"] = file_name
                dict_telemetry["test id"]["date"] = int(date.strftime("%Y%m%d"))
     
                with open(file_name, 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(setup.setup)
        except Exception as e:
                print("Error during setup of log")

def read_latest_line(ser,buffer_bytes,data):
        latest_received = data
        bytesToRead = ser.inWaiting()
        temp_bytes = ser.read(bytesToRead)
        buffer_bytes = buffer_bytes + temp_bytes
        buffer_string = buffer_bytes.decode()
        lines = buffer_string.split('\r\n')
        if len(lines) > 1:
            latest_received = lines[-2]
            buffer_bytes = temp_bytes
        else:
            print("Not enough serial input, using last available")
        return latest_received,buffer_bytes

def read_from_serial(ser,buffer_bytes):
        try:
                serial_data = []
                line,buffer_bytes = read_latest_line(ser,buffer_bytes)
                splitline = line.split(',')
                for x in splitline:
                        serial_data.append(float(x))
                
                ##Convert from g to m/s²
                #serial_data[1] = serial_data[1]*9.806
                #serial_data[2] = serial_data[2]*9.806
                #serial_data[3] = serial_data[3]*9.806

                return serial_data,buffer_bytes
        except Exception as e:
                print("Serial Read Error")
                
def dji_imu_callback(msg):
        dict_telemetry["dji imu"]["header"]["sequence"] = msg.header.seq
        dict_telemetry["dji imu"]["header"]["seconds"] = msg.header.stamp.secs
        dict_telemetry["dji imu"]["header"]["nanoseconds"] = msg.header.stamp.nsecs
        dict_telemetry["dji imu"]["header"]["frame id"] = msg.header.frame_id

        orientation = msg.orientation
        dict_telemetry["dji imu"]["orientation"]["x"] = orientation.x
        dict_telemetry["dji imu"]["orientation"]["y"] = orientation.y
        dict_telemetry["dji imu"]["orientation"]["z"] = orientation.z
        dict_telemetry["dji imu"]["orientation"]["w"] = orientation.w

        angular_velocity = msg.angular_velocity
        dict_telemetry["dji imu"]["angular velocity"]["x"] = angular_velocity.x
        dict_telemetry["dji imu"]["angular velocity"]["y"] = angular_velocity.y
        dict_telemetry["dji imu"]["angular velocity"]["z"] = angular_velocity.z

        linear_acceleration = msg.linear_acceleration
        dict_telemetry["dji imu"]["linear acceleration"]["x"] = linear_acceleration.x
        dict_telemetry["dji imu"]["linear acceleration"]["y"] = linear_acceleration.y
        dict_telemetry["dji imu"]["linear acceleration"]["z"] = linear_acceleration.z

def dji_joy_callback(msg):
        dict_telemetry["rc"]["header"]["sequence"] = msg.header.seq
        dict_telemetry["rc"]["header"]["seconds"] = msg.header.stamp.secs
        dict_telemetry["rc"]["header"]["nanoseconds"] = msg.header.stamp.nsecs
        dict_telemetry["rc"]["header"]["frame id"] = msg.header.frame_id
        
        dict_telemetry["rc"]["roll"]         = msg.axes[0]
        dict_telemetry["rc"]["pitch"]        = msg.axes[1]
        dict_telemetry["rc"]["yaw"]          = msg.axes[2]
        dict_telemetry["rc"]["throttle"]     = msg.axes[3]
        dict_telemetry["rc"]["mode"]         = msg.axes[4]
        dict_telemetry["rc"]["landing_gear"] = msg.axes[5]
		
def vicon_callback(msg):
        dict_telemetry["vicon"]["header"]["sequence"] = msg.header.seq
        dict_telemetry["vicon"]["header"]["seconds"] = msg.header.stamp.secs
        dict_telemetry["vicon"]["header"]["nanoseconds"] = msg.header.stamp.nsecs
        dict_telemetry["vicon"]["header"]["frame id"] = msg.header.frame_id

        dict_telemetry["vicon"]["child frame id"] = msg.child_frame_id
                
        dict_telemetry["vicon"]["translation"]["x"] = msg.transform.translation.x
        dict_telemetry["vicon"]["translation"]["y"] = msg.transform.translation.y
        dict_telemetry["vicon"]["translation"]["z"] = msg.transform.translation.z
        dict_telemetry["vicon"]["rotation"]["x"] = msg.transform.rotation.x
        dict_telemetry["vicon"]["rotation"]["y"] = msg.transform.rotation.y
        dict_telemetry["vicon"]["rotation"]["z"] = msg.transform.rotation.z
        dict_telemetry["vicon"]["rotation"]["w"] = msg.transform.rotation.w
        
def namer():
        file_name = 0
        while file_name == 0:
                name = input("enter desired filename. ")
                csv_name = name + ".csv"
                if os.path.isfile(csv_name):
                        cmd = input("A file with that name already exists. Overwrite file? [y/n] ")
                        if cmd == "y" or cmd == "Y":
                                os.remove(csv_name)
                                file_name = csv_name
                        elif cmd == "n" or cmd == "N":
                                print("Choose another filename")
                                file_name = 0
                        else:
                                exit(0)
                else:
                        file_name = csv_name
        return(file_name)

if __name__ == '__main__':
        rospy.init_node('Telemetry_logger', anonymous=True)
        rospy.Subscriber("/dji_sdk/imu", Imu, dji_imu_callback)
        rospy.Subscriber("/dji_sdk/rc", Joy, dji_joy_callback)
        rospy.Subscriber("/vicon/test_obj/test_obj", TransformStamped, vicon_callback)
        rate = rospy.Rate(50) # hz

        file_name = namer()
        logsetup()
        
        max_cycle = 0
        min_cycle = 10
        timer_i = 0

        while True:
                beginTime = time.time()
                int_imu_data = [0,1,2,3,4,5,6,7,8,9] 
                #int_imu_data,buffer_bytes1 = read_from_serial(ser1,buffer_bytes1,int_imu_data)
                ext_imu_data,buffer_bytes2 = read_from_serial(ser2,buffer_bytes2,ext_imu_data)
                log(int_imu_data,ext_imu_data)
                rate.sleep()
                
                timer_i = timer_i+1
                cycle = time.time()-beginTime
                if max_cycle < cycle:
                        max_cycle = cycle
                if min_cycle > cycle:
                        min_cycle = cycle
                #print(max_cycle)
                #print(min_cycle)
                if  timer_i % 200 == 0:
                        max_cycle = 0
                        min_cycle = 10
                



























