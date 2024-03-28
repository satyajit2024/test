import socket
import time
from pymavlink import mavutil

# TCP server settings
TCP_IP = '127.0.0.1'  # IP address of the TCP server
TCP_PORT = 5760  # MAVLink default port

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

# Create a MAVLink connection using the TCP socket
mavlink_conn = mavutil.mavlink_connection(sock)

# Send a MAVLink heartbeat message
mavlink_conn.mav.heartbeat_send(
    mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

# Send a MAVLink message with some data (example: attitude message)
roll = 0.1  # Roll angle in radians
pitch = 0.2  # Pitch angle in radians
yaw = 0.3  # Yaw angle in radians

# Create an attitude message
msg = mavlink_conn.mav.attitude_target_encode(
    time.time(),  # Timestamp
    1,  # Target system ID
    1,  # Target component ID
    0b11111111,  # Target mode bits (all set to 1 for full control)
    [roll, pitch, yaw],  # Attitude quaternion
    0, 0, 0,  # Body rates (not used in this example)
)

# Send the attitude message
mavlink_conn.send(msg)

# Close the TCP socket
sock.close()
