#!/usr/bin/env python3

import os
import rospy
import time
import json
import pprint

from json_setup 	import telemetry
from sensor_msgs.msg 	import BatteryState
from sensor_msgs.msg 	import NavSatFix
from sensor_msgs.msg    import Imu
from geometry_msgs.msg 	import Vector3Stamped
from geometry_msgs.msg 	import PointStamped
from std_msgs.msg       import UInt8
from std_msgs.msg       import Float32
from sensor_msgs.msg    import Joy
import std_msgs.msg

dict_telemetry = telemetry
filename = "temp/Telemetry.json"
pp = pprint.PrettyPrinter(indent=4)

def battery_callback(msg):
	if (msg.voltage >= 0):
		dict_telemetry["battery"]["voltage"] 		= msg.voltage
	if (msg.current >= 0):
		dict_telemetry["battery"]["current"] 		= msg.current
	if (msg.charge >= 0):
		dict_telemetry["battery"]["charge"]  		= msg.charge
	if (msg.capacity >= 0):
		dict_telemetry["battery"]["capacity"]		= msg.capacity
	if (msg.design_capacity >= 0):
		dict_telemetry["battery"]["design_capacity"]	= msg.design_capacity
	if (msg.percentage >= 0):
		dict_telemetry["battery"]["level"] 			= msg.percentage
#	if (msg.voltage[0] >= 0):
#		dict_telemetry["battery"]["battery_cell_1"] = msg.cell_voltage[0]
#	if (msg.voltage[1] >= 0):
#		dict_telemetry["battery"]["battery_cell_2"] = msg.cell_voltage[1]
#	if (msg.voltage[2] >= 0):
#		dict_telemetry["battery"]["battery_cell_3"] = msg.cell_voltage[2]
#	if (msg.voltage[3] >= 0):
#		dict_telemetry["battery"]["battery_cell_4"] = msg.cell_voltage[3]
#	if (msg.voltage[4] >= 0):
#		dict_telemetry["battery"]["battery_cell_5"] = msg.cell_voltage[4]
#	if (msg.voltage[5] >= 0):
#		dict_telemetry["battery"]["battery_cell_6"] = msg.cell_voltage[5]

def gps_health_callback(data):
	if (data.data >= 0):
		dict_telemetry["gps"]["health"] = data.data

def gps_position_callback(msg):
	if (msg.status.status >= 0):
		dict_telemetry["gps"]["nsat"]	  = msg.status.status
	if (msg.latitude >= 0):
		dict_telemetry["location"]["lat"] = msg.latitude
	if (msg.longitude >= 0):
		dict_telemetry["location"]["lon"] = msg.longitude
	if (msg.altitude >= 0):
		dict_telemetry["location"]["alt"] = msg.altitude
#	if (msg.position_covariance >= 0):
#		dict_telemetry["heading"]         = msg.position_covariance

def velocity_callback(msg):
	velocity = msg.vector
	if (msg.vector.x >= 0):
		dict_telemetry["velocity"]["x"] = msg.vector.x
	if (msg.vector.y >= 0):
		dict_telemetry["velocity"]["y"] = msg.vector.y
	if (msg.vector.z >= 0):
		dict_telemetry["velocity"]["z"] = msg.vector.z

def height_callback(data):
	if (data.data >= 0):
		dict_telemetry["height_above_takeoff"] = data.data

def local_position_callback(msg):
	point = msg.point
	if (point.x >= 0):
		dict_telemetry["calculated"]["roll"] 	= point.x
	if (point.y >= 0):
		dict_telemetry["calculated"]["pitch"] 	= point.y
	if (point.z >= 0):
		dict_telemetry["calculated"]["yaw"]	= point.z

def joy_callback(msg):
	if (msg.axes[0] >= 0):
		dict_telemetry["rc"]["roll"]         = msg.axes[0]
	if (msg.axes[1] >= 0):
		dict_telemetry["rc"]["pitch"]        = msg.axes[1]
	if (msg.axes[2] >= 0):
		dict_telemetry["rc"]["yaw"]          = msg.axes[2]
	if (msg.axes[3] >= 0):
		dict_telemetry["rc"]["throttle"]     = msg.axes[3]
	if (msg.axes[4] >= 0):
		dict_telemetry["rc"]["mode"]         = msg.axes[4]
	if (msg.axes[5] >= 0):
		dict_telemetry["rc"]["landing_gear"] = msg.axes[5]

def imu_callback(msg):
	orientation = msg.orientation
	if (orientation.x >= 0):
		dict_telemetry["imu"]["orientation"]["x"] = orientation.x
	if (orientation.y >= 0):
		dict_telemetry["imu"]["orientation"]["y"] = orientation.y
	if (orientation.z >= 0):
		dict_telemetry["imu"]["orientation"]["z"] = orientation.z

	angular_velocity = msg.angular_velocity
	if (angular_velocity.x >= 0):
		dict_telemetry["imu"]["velocity"]["x"] = angular_velocity.x
	if (angular_velocity.y >= 0):
		dict_telemetry["imu"]["velocity"]["y"] = angular_velocity.y
	if (angular_velocity.z >= 0):
		dict_telemetry["imu"]["velocity"]["z"] = angular_velocity.z

	linear_acceleration = msg.linear_acceleration
	if (linear_acceleration.x >= 0):
		dict_telemetry["imu"]["acceleration"]["x"] = linear_acceleration.x
	if (linear_acceleration.y >= 0):
		dict_telemetry["imu"]["acceleration"]["y"] = linear_acceleration.y
	if (linear_acceleration.z >= 0):
		dict_telemetry["imu"]["acceleration"]["z"] = linear_acceleration.z

def display_mode_callback(data):
	if (data.data == 1):
		task = "GOHOME"
	elif (data.data == 4):
		task = "TAKEOFF"
	elif (data.data == 6):
		task = "LAND"
	dict_telemetry["mode"] = task

def flight_status_callback(data):
	if (data.data == 0):
		mode = "ON_GROUND"
	else:
		mode = "ACTIVE"
	dict_telemetry["status"] = mode


def telemetry_json():
	while not rospy.is_shutdown():
		with open(filename, 'w') as f:
			json.dump(dict_telemetry, f)

#def read_from_safeeye():
#	line = ser.readline()
#	j = ""
#	try:
#		j = json.loads(line.decode())
#		if j['type'] == 'fft':
#			dict_telemetry.update(j) 
#	except Exception as e:
#		print("Something happened")

if __name__ == '__main__':
  rospy.init_node('Telemetry_json', anonymous=True)
  rospy.Subscriber("/dji_sdk/battery_state", BatteryState, battery_callback)
  rospy.Subscriber("/dji_sdk/gps_health", UInt8, gps_health_callback)
  rospy.Subscriber("/dji_sdk/gps_position", NavSatFix, gps_position_callback)
  rospy.Subscriber("/dji_sdk/velocity", Vector3Stamped, velocity_callback)
  rospy.Subscriber("/dji_sdk/height_above_takeoff", Float32 , height_callback)
  rospy.Subscriber("/dji_sdk/local_position", PointStamped, local_position_callback)
  rospy.Subscriber("/dji_sdk/rc", Joy, joy_callback)
  rospy.Subscriber("/dji_sdk/imu", Imu, imu_callback)
#  rospy.Subscriber("/dji_sdk/display_mode", UInt8 , display_mode_callback)
  rospy.Subscriber("/dji_sdk/flight_status", UInt8 , flight_status_callback)

  try:
    telemetry_json()
  except rospy.ROSInterruptException:
    pass
