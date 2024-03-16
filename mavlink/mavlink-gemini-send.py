import socket  # Import the socket library
from pymavlink import mavutil
import time
# Define system and component IDs (change if needed)
sysid = 1
compid = mavutil.mavlink.MAV_COMP_ID_GIMBAL  # Assuming Gimbal component

# Define UDP connection details (localhost and port - change port if needed)
server_address = ("192.168.240.153", 14550)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Create a heartbeat message
while True:
    msg = mavutil.mavlink.MAVLink_command_long_message(
        target_system=1,        # Target system ID
        target_component=compid,   # Target component ID
        command=400,            # Command ID, refer to MAV_CMD enumeration for specific command
        # Confirmation for command acceptance (set to 0 for no confirmation)
        confirmation=0,
        param1=0.0,             # Command-specific parameter 1
        param2=0.0,             # Command-specific parameter 2
        param3=0.0,             # Command-specific parameter 3
        param4=0.0,             # Command-specific parameter 4
        param5=0.0,             # Command-specific parameter 5
        param6=0.0,             # Command-specific parameter 6
        param7=0.0              # Command-specific parameter 7
    )

    print("Before pack.....", msg)
    print("type.....", type(msg))
    # data = str(msg)
    # Pack the message
    # '2' is the mavlink version, '1' is the system ID
    data = msg.pack(mavutil.mavlink.MAVLink('', 2, 1))
    print("After pack.....", data)

    # sock.sendto(data.encode("utf-8"), server_address)
    sock.sendto(data, server_address)

    # Close the socket
    # sock.close()

    print("Sent heartbeat message! \n")
    time.sleep(1)
