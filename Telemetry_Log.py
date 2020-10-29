#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 28, 2020 05:47:52 PM CEST  platform: Windows NT

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import sys, os.path, time, rospy, serial, datetime, setup, csv
from json_setup import telemetry
from tkinter.filedialog import asksaveasfile
from sensor_msgs.msg import Imu
from sensor_msgs.msg import Joy
from geometry_msgs.msg import TransformStamped

prog_call = sys.argv[0]
prog_location = os.path.split(prog_call)[0]
dict_telemetry = telemetry
toLog = False
#ser1 = serial.Serial('/dev/ttyS2',115200)
#ser1 = serial.Serial('/dev/ttyACM0',115200)
ser2 = serial.Serial('/dev/ttyACM0',115200)
latest_received = '0,0,0,0,0,0,0,0,0,0'
buffer_bytes = b''

class Toplevel1:
    def __init__(self, top=None):
        global x
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 13 -weight bold"
        font8 = "-family {Segoe UI} -size 11 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32": self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

        top.geometry("605x475+747+239")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(0, 0)
        top.title("Vibration Log")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.top = top

        self.DJI_Remote_Image = tk.Label(top)
        self.DJI_Remote_Image.place(relx=0.302, rely=-0.03, height=402
                , width=440)
        self.DJI_Remote_Image.configure(activebackground="#f9f9f9")
        self.DJI_Remote_Image.configure(activeforeground="black")
        self.DJI_Remote_Image.configure(background="#d9d9d9")
        self.DJI_Remote_Image.configure(disabledforeground="#a3a3a3")
        self.DJI_Remote_Image.configure(foreground="#000000")
        self.DJI_Remote_Image.configure(highlightbackground="#d9d9d9")
        self.DJI_Remote_Image.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"Icons/DJI_Remote-removebg-preview.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.DJI_Remote_Image.configure(image=_img0)
        self.DJI_Remote_Image.configure(text='''Label''')

        self.Yaw_Level = ttk.Progressbar(top)
        self.Yaw_Level.place(relx=0.645, rely=0.484, relwidth=0.167
                , relheight=0.0, height=22)
        self.Yaw_Level.configure(mode="indeterminate")
        self.Yaw_Level.configure(maximum="2")
        self.Yaw_Level.configure(value="1")

        self.Throttle_Level = ttk.Progressbar(top)
        self.Throttle_Level.place(relx=0.711, rely=0.4, relwidth=0.036
                , relheight=0.0, height=105)
        self.Throttle_Level.configure(orient="vertical")
        self.Throttle_Level.configure(mode="indeterminate")
        self.Throttle_Level.configure(maximum="2")
        self.Throttle_Level.configure(value="1")

        self.Roll_level = ttk.Progressbar(top)
        self.Roll_level.place(relx=0.81, rely=0.484, relwidth=0.167
                , relheight=0.0, height=23)
        self.Roll_level.configure(mode="indeterminate")
        self.Roll_level.configure(maximum="2")
        self.Roll_level.configure(value="1")

        self.Pitch_level = ttk.Progressbar(top)
        self.Pitch_level.place(relx=0.876, rely=0.4, relwidth=0.036
                , relheight=0.0, height=105)
        self.Pitch_level.configure(orient="vertical")
        self.Pitch_level.configure(mode="indeterminate")
        self.Pitch_level.configure(maximum="2")
        self.Pitch_level.configure(value="1")

        self.A3_Image = tk.Label(top)
        self.A3_Image.place(relx=0.017, rely=0.526, height=159, width=195)
        self.A3_Image.configure(activebackground="#f9f9f9")
        self.A3_Image.configure(activeforeground="black")
        self.A3_Image.configure(background="#d9d9d9")
        self.A3_Image.configure(disabledforeground="#a3a3a3")
        self.A3_Image.configure(foreground="#000000")
        self.A3_Image.configure(highlightbackground="#d9d9d9")
        self.A3_Image.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"Icons/A3-removebg-preview.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.A3_Image.configure(image=_img1)
        self.A3_Image.configure(text='''Label''')

        self.Nanopi_image = tk.Label(top)
        self.Nanopi_image.place(relx=0.017, rely=0.043, height=200, width=201)
        self.Nanopi_image.configure(activebackground="#f9f9f9")
        self.Nanopi_image.configure(activeforeground="black")
        self.Nanopi_image.configure(background="#d9d9d9")
        self.Nanopi_image.configure(disabledforeground="#a3a3a3")
        self.Nanopi_image.configure(foreground="#000000")
        self.Nanopi_image.configure(highlightbackground="#d9d9d9")
        self.Nanopi_image.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"Icons/nanopi-removebg-preview.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Nanopi_image.configure(image=_img2)
        self.Nanopi_image.configure(text='''Label''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Acceleration_x = ttk.Label(top)
        self.Acceleration_x.place(relx=0.017, rely=0.863, height=19, width=195)
        self.Acceleration_x.configure(background="#d9d9d9")
        self.Acceleration_x.configure(foreground="#000000")
        self.Acceleration_x.configure(font="TkDefaultFont")
        self.Acceleration_x.configure(relief="flat")
        self.Acceleration_x.configure(anchor='w')
        self.Acceleration_x.configure(justify='left')
        self.Acceleration_x.configure(text='''Acceleration X:''')

        self.Acceleration_y = ttk.Label(top)
        self.Acceleration_y.place(relx=0.017, rely=0.905, height=19, width=195)
        self.Acceleration_y.configure(background="#d9d9d9")
        self.Acceleration_y.configure(foreground="#000000")
        self.Acceleration_y.configure(font="TkDefaultFont")
        self.Acceleration_y.configure(relief="flat")
        self.Acceleration_y.configure(anchor='w')
        self.Acceleration_y.configure(justify='left')
        self.Acceleration_y.configure(text='''Acceleration Y:''')

        self.Acceleration_z = ttk.Label(top)
        self.Acceleration_z.place(relx=0.017, rely=0.947, height=19, width=195)
        self.Acceleration_z.configure(background="#d9d9d9")
        self.Acceleration_z.configure(foreground="#000000")
        self.Acceleration_z.configure(font="TkDefaultFont")
        self.Acceleration_z.configure(relief="flat")
        self.Acceleration_z.configure(anchor='w')
        self.Acceleration_z.configure(justify='left')
        self.Acceleration_z.configure(text='''Acceleration Z:''')

        self.Bin_Values = ttk.Label(top)
        self.Bin_Values.place(relx=0.364, rely=0.021, height=369, width=155)
        self.Bin_Values.configure(background="#d9d9d9")
        self.Bin_Values.configure(foreground="#000000")
        self.Bin_Values.configure(font="TkDefaultFont")
        self.Bin_Values.configure(relief="flat")
        self.Bin_Values.configure(anchor='nw')
        self.Bin_Values.configure(justify='left')
        self.Bin_Values.configure(text='''Bin_Value''')

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.347, rely=0.526, relheight=0.484)
        self.TSeparator2.configure(orient="vertical")

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=-0.017, rely=0.526, relwidth=0.647)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.628, rely=-0.021, relheight=1.032)
        self.TSeparator1.configure(orient="vertical")

        self.Throttle = tk.Label(top)
        self.Throttle.place(relx=0.645, rely=0.8, height=21, width=205)
        self.Throttle.configure(activebackground="#f9f9f9")
        self.Throttle.configure(activeforeground="black")
        self.Throttle.configure(anchor='w')
        self.Throttle.configure(background="#d9d9d9")
        self.Throttle.configure(disabledforeground="#a3a3a3")
        self.Throttle.configure(foreground="#000000")
        self.Throttle.configure(highlightbackground="#d9d9d9")
        self.Throttle.configure(highlightcolor="black")
        self.Throttle.configure(text='''Throttle:''')

        self.Yaw = tk.Label(top)
        self.Yaw.place(relx=0.645, rely=0.842, height=21, width=205)
        self.Yaw.configure(activebackground="#f9f9f9")
        self.Yaw.configure(activeforeground="black")
        self.Yaw.configure(anchor='w')
        self.Yaw.configure(background="#d9d9d9")
        self.Yaw.configure(disabledforeground="#a3a3a3")
        self.Yaw.configure(foreground="#000000")
        self.Yaw.configure(highlightbackground="#d9d9d9")
        self.Yaw.configure(highlightcolor="black")
        self.Yaw.configure(text='''Yaw:''')

        self.Pitch = tk.Label(top)
        self.Pitch.place(relx=0.645, rely=0.884, height=21, width=205)
        self.Pitch.configure(activebackground="#f9f9f9")
        self.Pitch.configure(activeforeground="black")
        self.Pitch.configure(anchor='w')
        self.Pitch.configure(background="#d9d9d9")
        self.Pitch.configure(disabledforeground="#a3a3a3")
        self.Pitch.configure(foreground="#000000")
        self.Pitch.configure(highlightbackground="#d9d9d9")
        self.Pitch.configure(highlightcolor="black")
        self.Pitch.configure(text='''Pitch:''')

        self.Roll = tk.Label(top)
        self.Roll.place(relx=0.645, rely=0.926, height=21, width=205)
        self.Roll.configure(activebackground="#f9f9f9")
        self.Roll.configure(activeforeground="black")
        self.Roll.configure(anchor='w')
        self.Roll.configure(background="#d9d9d9")
        self.Roll.configure(disabledforeground="#a3a3a3")
        self.Roll.configure(foreground="#000000")
        self.Roll.configure(highlightbackground="#d9d9d9")
        self.Roll.configure(highlightcolor="black")
        self.Roll.configure(text='''Roll:''')

        self.Log_Button = tk.Button(top)
        self.Log_Button.place(relx=0.364, rely=0.905, height=34, width=157)
        self.Log_Button.configure(activebackground="#ececec")
        self.Log_Button.configure(activeforeground="#000000")
        self.Log_Button.configure(background="#d9d9d9")
        self.Log_Button.configure(disabledforeground="#a3a3a3")
        self.Log_Button.configure(foreground="#000000")
        self.Log_Button.configure(highlightbackground="#d9d9d9")
        self.Log_Button.configure(highlightcolor="black")
        self.Log_Button.configure(pady="0")
        self.Log_Button.configure(text='''Start Logging''')
        self.Log_Button["command"] = self.logData

        self.Text_Label = tk.Label(top)
        self.Text_Label.place(relx=0.364, rely=0.821, height=31, width=154)
        self.Text_Label.configure(activebackground="#00ff00")
        self.Text_Label.configure(activeforeground="#000000")
        self.Text_Label.configure(background="#00ff00")
        self.Text_Label.configure(compound='center')
        self.Text_Label.configure(disabledforeground="#a3a3a3")
        self.Text_Label.configure(font=font9)
        self.Text_Label.configure(foreground="#000000")
        self.Text_Label.configure(relief="sunken")
        self.Text_Label.configure(text='''Ready''')

    def onOpen(self):
        try:
                self.Yaw_Level.configure(value=(dict_telemetry["rc"]["yaw"])+1)
                self.Throttle_Level.configure(value=(dict_telemetry["rc"]["throttle"] * -1)+1)
                self.Roll_level.configure(value=(dict_telemetry["rc"]["roll"])+1)
                self.Pitch_level.configure(value=(dict_telemetry["rc"]["pitch"] * -1)+1)
                self.Acceleration_x.configure(text=str("Acceleration X: " + str(dict_telemetry["dji imu"]["linear acceleration"]["x"])))
                self.Acceleration_y.configure(text=str("Acceleration Y: " + str(dict_telemetry["dji imu"]["linear acceleration"]["y"])))
                self.Acceleration_z.configure(text=str("Acceleration Z: " + str(dict_telemetry["dji imu"]["linear acceleration"]["z"])))
                self.Throttle.configure(text=str("Throttle : " + str(dict_telemetry["rc"]["throttle"])))
                self.Yaw.configure(text=str("Yaw: " + str(dict_telemetry["rc"]["yaw"])))
                self.Pitch.configure(text=str("Pitch: " + str(dict_telemetry["rc"]["pitch"])))
                self.Roll.configure(text=str("Roll: " + str(dict_telemetry["rc"]["roll"])))
                int_imu_data = [0,1,2,3,4,5,6,7,8,9] #read_from_serial(ser1)
                ext_imu_data = read_from_serial(ser2)
                self.Bin_Values.configure(text=str("X: " + str(int_imu_data[1]) + "\nY: " + str(int_imu_data[2]) + "\nZ: " + str(int_imu_data[3])))
                if toLog == True:
                        self.log(int_imu_data, ext_imu_data)
        except Exception as e:
                print("Main Loop Error")

    def refresh(self):
        root.update_idletasks()
        root.update()
        #time.sleep(0.01)

    def logData(self):
        global file_name, toLog
        try:
            if toLog == False:
                files = [('CSV File', '*.csv')]
                file_name = asksaveasfile(filetypes=files, defaultextension=files).name
                toLog = True
                self.Text_Label.configure(background="#ffff00")
                self.Text_Label.configure(text='''Logging''')
                self.Log_Button.configure(text='''Stop Logging''')
                #Define header for csv file
                logsetup()
                                
            elif toLog == True:
                toLog = False
                self.Text_Label.configure(background="#00ff00")
                self.Text_Label.configure(text='''Ready''')
                self.Log_Button.configure(text='''Start Logging''')
        except Exception as e:
            print("No valid savefile")
            self.Text_Label.configure(background="#ffff00")
            self.Text_Label.configure(text='''Invalid savefile''')
            
    def log(self, data1, data2):
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
                print(field_ext_imu)
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
        try:
                serial_data = []
                line = read_latest_line(ser)
                splitline = line.split(',')
                for x in splitline:
                        serial_data.append(float(x))
                
                ##Convert from g to m/s²
                #serial_data[1] = serial_data[1]*9.806
                #serial_data[2] = serial_data[2]*9.806
                #serial_data[3] = serial_data[3]*9.806

                return serial_data
        except Exception as e:
                print("Serial Read Error")
                
def execution_timer():
        timer_i = timer_i+1
        cycle = time.time()-beginTime
        if max_cycle < cycle:
                max_cycle = cycle
        if min_cycle > cycle:
                min_cycle = cycle
        print(max_cycle)
        print(min_cycle)
        if  timer_i % 20 == 0:
                max_cycle = 0
                min_cycle = 10
                
           

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
        

if __name__ == '__main__':
        root = tk.Tk()
        app = Toplevel1(top=root)

        rospy.init_node('Telemetry_logger', anonymous=True)
        rospy.Subscriber("/dji_sdk/imu", Imu, dji_imu_callback)
        rospy.Subscriber("/dji_sdk/rc", Joy, dji_joy_callback)
        rospy.Subscriber("/vicon/test_obj/test_obj", TransformStamped, vicon_callback)
        rate = rospy.Rate(10) # hz
        
        max_cycle = 0
        min_cycle = 10
        timer_i = 0

        while True:
                beginTime = time.time()
                app.refresh()
                app.onOpen()
                rate.sleep()
                #execution_timer()
                



























