import socket  # Import the socket library
from pymavlink import mavutil
import time
# Define system and component IDs (change if needed)
sysid = 1
compid = mavutil.mavlink.MAV_COMP_ID_GIMBAL  # Assuming Gimbal component

# Define UDP connection details (localhost and port - change port if needed)
server_address = ("192.168.0.121", 14550)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Create a heartbeat message
while True:
    msg = mavutil.mavlink.MAVLink_heartbeat_message(
        type=mavutil.mavlink.MAV_TYPE_GCS,  # or MAV_TYPE_ONBOARD_CONTROLLER if applicable
        autopilot=mavutil.mavlink.MAV_AUTOPILOT_INVALID,
        base_mode=mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
        custom_mode=0,  # MAV_MODE_FLAG_TEST_ENABLED
        system_status=0,  # MAV_MODE_FLAG_AUTO_ENABLED
        mavlink_version=2,  # MAV_MODE_FLAG_GUIDED_ENABLED
    )

    print("Before pack.....",msg)
    print("type.....",type(msg))
    # data = str(msg)
    # Pack the message
    data = msg.pack(mavutil.mavlink.MAVLink('', 2, 1))  # '2' is the mavlink version, '1' is the system ID
    print("After pack.....",data)

    # sock.sendto(data.encode("utf-8"), server_address)
    sock.sendto(data, server_address)

    # Close the socket
    # sock.close()

    print("Sent heartbeat message! \n")
    time.sleep(1)

