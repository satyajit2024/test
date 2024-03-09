# MAVLink 

- MAVLink (Micro Air Vehicle Link) is a lightweight communication protocol designed for unmanned vehicles. It’s used extensively in the drone industry to facilitate communication between various components such as flight controllers, ground control stations, and payload systems. 

## Key Features: 

- Lightweight: Optimized for bandwidth-constrained and unreliable links. 

- Extensible: Supports different types of vehicles and payloads. 

- Standardized: Widely adopted, ensuring interoperability between different systems. 

- Usage: MAVLink is used for sending commands to drones, receiving telemetry data, and managing the drone’s operation in real-time. 

 

## Pymavlink 

- Pymavlink is a Python implementation of the MAVLink protocol. It serves as a low-level and general-purpose library for MAVLink message processing. 

## Key Features: 

- Python-based: Easy integration with Python applications and scripts. 

- Support for MAVLink 1 and 2: Compatible with both versions of the MAVLink protocol. 

- General-purpose: Can be used across various MAVLink-compatible systems. 

- Usage: Pymavlink is utilized in creating ground control stations, developing APIs like DroneKit, and building companion computer applications for drones. 

- MAVLink messages are a crucial part of the protocol, allowing various systems to communicate by exchanging information like commands, data, and statuses. Each message type in MAVLink has a specific structure and requires certain parameters. Here’s a high-level overview of some common MAVLink message types and their parameters: 

 

# Common MAVLink Message Types 

### HEARTBEAT 

- Parameters: type, autopilot, base_mode, custom_mode, system_status, mavlink_version 

- Description: Indicates the presence of a system and its current status. 

## SYS_STATUS 

- Parameters: onboard_control_sensors_present, onboard_control_sensors_enabled, onboard_control_sensors_health, load, voltage_battery, current_battery, battery_remaining, drop_rate_comm, errors_comm, errors_count1, errors_count2, errors_count3, errors_count4 

- Description: Provides a comprehensive system status, including battery and communication information. 

## GPS_RAW_INT 

- Parameters: time_usec, fix_type, lat, lon, alt, eph, epv, vel, cog, satellites_visible 

- Description: Contains raw GPS data like position, velocity, and satellite details. 

## ATTITUDE 

- Parameters: time_boot_ms, roll, pitch, yaw, rollspeed, pitchspeed, yawspeed 

- Description: Provides the system’s current attitude, including roll, pitch, and yaw angles. 

## MISSION_ITEM 

- Parameters: seq, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z 

- Description: Describes a mission item or waypoint. 

## COMMAND_LONG 

- Parameters: target_system, target_component, command, confirmation, param1, param2, param3, param4, param5, param6, param7 

- Description: Sends a command with up to seven parameters to a target system or component. 

## PARAM_VALUE 

- Parameters: param_id, param_value, param_type, param_count, param_index 

- Description: Transmits the value of a parameter with its index and total count. 

 

- Adding Parameters to Messages: When constructing a MAVLink message, you need to ensure that all required parameters are included and correctly formatted according to the message type’s specification. The parameters often include values like system state, GPS coordinates, mission commands, and more. 

# HEARTBEAT Message Example: 
```bash
mavlink_connection.mav.heartbeat_send( 

    type=MAV_TYPE_QUADROTOR,  

    autopilot=MAV_AUTOPILOT_GENERIC,  

    base_mode=MAV_MODE_GUIDED_ARMED,  

    custom_mode=0,  

    system_status=MAV_STATE_ACTIVE,  

    mavlink_version=3 

) 

  

SYS_STATUS Message Example: 

mavlink_connection.mav.sys_status_send( 

    onboard_control_sensors_present=SENSOR_GPS | SENSOR_ACCEL | SENSOR_GYRO | SENSOR_MAG,  

    onboard_control_sensors_enabled=SENSOR_GPS | SENSOR_ACCEL | SENSOR_GYRO | SENSOR_MAG,  

    onboard_control_sensors_health=SENSOR_GPS | SENSOR_ACCEL | SENSOR_GYRO | SENSOR_MAG,  

    load=500,  

    voltage_battery=11000,  

    current_battery=1200,  

    battery_remaining=70,  

    drop_rate_comm=0,  

    errors_comm=0,  

    errors_count1=0,  

    errors_count2=0,  

    errors_count3=0,  

    errors_count4=0 

) 

  

GPS_RAW_INT Message Example: 

mavlink_connection.mav.gps_raw_int_send( 

    time_usec=123456789,  

    fix_type=GPS_FIX_TYPE_3D_FIX,  

    lat=475012345,  

    lon=853212345,  

    alt=10000,  

    eph=175,  

    epv=270,  

    vel=65,  

    cog=135,  

    satellites_visible=10 

) 

  

ATTITUDE Message Example: 

mavlink_connection.mav.attitude_send( 

    time_boot_ms=123456789,  

    roll=0.1,  

    pitch=0.2,  

    yaw=1.5,  

    rollspeed=0.01,  

    pitchspeed=0.02,  

    yawspeed=0.03 

) 

  

MISSION_ITEM Message Example: 

mavlink_connection.mav.mission_item_send( 

    seq=2,  

    frame=MAV_FRAME_GLOBAL_RELATIVE_ALT,  

    command=MAV_CMD_NAV_WAYPOINT,  

    current=0,  

    autocontinue=1,  

    param1=0,  

    param2=0,  

    param3=0,  

    param4=0,  

    x=47.3977418,  

    y=8.5455932,  

    z=10 

) 

  

COMMAND_LONG Message Example: 

mavlink_connection.mav.command_long_send( 

    target_system=1,  

    target_component=1,  

    command=MAV_CMD_DO_SET_MODE,  

    confirmation=0,  

    param1=MAV_MODE_AUTO_ARMED,  

    param2=0,  

    param3=0,  

    param4=0,  

    param5=0,  

    param6=0,  

    param7=0 

) 

  

PARAM_VALUE Message Example: 

mavlink_connection.mav.param_value_send( 

    param_id='SYSID_THISMAV',  

    param_value=1,  

    param_type=MAV_PARAM_TYPE_UINT8,  

    param_count=100,  

    param_index=50 

) 
```