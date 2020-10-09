telemetry_old = {
    "battery": {
        "voltage": 0.0,
        "current": 0.0,
        "charge": 0.0,
        "capacity": 0.0,
        "design_capacity": 0.0,
        "level": 0.0,
		"battery_cell_1": 0.0,
		"battery_cell_2": 0.0,
		"battery_cell_3": 0.0,
		"battery_cell_4": 0.0,
		"battery_cell_5": 0.0,
		"battery_cell_6": 0.0},
		
    "location": {
        "lat": 0.0,
        "lon": 0.0,
        "alt": 0.0},
		
    "gps": {
        "health": 0.0,
        "fix": 0.0,
        "nsat": 0.0},
		
    "attitude": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0},
		
    "calculated": {
        "roll": 0.0,
        "pitch": 0.0,
        "yaw": 0.0},
		
    "rc": {
        "roll": 0.0,
        "pitch": 0.0,
        "yaw": 0.0,
        "throttle": 0.0,
        "mode": 0.0,
        "landing_gear": 0.0},
		
    "velocity": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0},
		
    "height_above_takeoff": 0.0,
	
    "imu": {
        "orientation": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0},
        "velocity": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0},
        "acceleration": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0}},
	"heading": 0.0,
	"status": "",
	"mode": "",
}

#---------------------------------------------------------------------------

telemetry = {
    "test id": 
	{
	"name": 0.0,
	"date": 0.0,
	"start time": 0.0,
	"duration": 0.0
	},
    "vicon":
	{
	"header":
	    {
	    "sequence": [],
	    "time stamp": [],
	    "frame id":[]
	    },
	"translation": 
	    {
	    "x": [],
	    "y": [],
	    "z": []
	    },
	"rotation":
	    {
	    "x": [],
	    "y": [],
	    "z": [],
	    "w": []
	    }
	},
    "internal imu": 
    	{
    	"header":
    	    {
    	    "time stamp": []
    	    },
        "accelerometer": 
            {
            "x": [],
            "y": [],
            "z": []
            },
        "gyrometer": 
            {
            "x": [],
            "y": [],
            "z": []
            },
        "magnetometer": 
            {
            "x": [],
            "y": [],
            "z": []
            }
        },
    "external imu": 
    	{
    	"header":
    	    {
    	    "time stamp": []
    	    },
        "accelerometer": 
            {
            "x": [],
            "y": [],
            "z": []
            },
        "gyrometer": 
            {
            "x": [],
            "y": [],
            "z": []
            },
        "magnetometer": 
            {
            "x": [],
            "y": [],
            "z": []
            }
        },
    "dji imu": 
    	{
    	"header":
	    {
	    "sequence": [],
	    "time stamp": [],
	    "frame id":[]
	    },
        "orientation": 
            {
            "x": [],
            "y": [],
            "z": []
            },
        "angular velocity": 
            {
            "x": [],
            "y": [],
            "z": []
            },
        "linear acceleration": 
            {
            "x": [],
            "y": [],
            "z": []
            }
        },
    "rc": 
        {
        "header":
            {
            "sequence": [],
	    "time stamp": [],
	    "frame id":[]
	    },
        "roll": [],
        "pitch": [],
        "yaw": [],
        "throttle": [],
        "mode": 0.0,
        "landing_gear": 0.0
        },
}





