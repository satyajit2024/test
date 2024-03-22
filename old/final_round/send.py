import socket
import time
from pymavlink import mavutil

# Get the public URL from ngrok (e.g., 0.tcp.ngrok.io:12345)
ngrok_url = "localhost:5000"

# Create a TCP socket and connect to the server
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((ngrok_url.split(":")[0], int(ngrok_url.split(":")[1])))

# Create a MAVLink connection over the TCP socket
master = mavutil.mavlink_connection(
    f"tcp:{ngrok_url.split(':')[0]}:{ngrok_url.split(':')[1]}", source_system=1, dialects=['common', 'px4']
)

while True:
    # Create a MAVLink message
    msg = mavutil.mavlink.MAVLink_command_long_message(
        target_system=1,        # Target system ID
        target_component=2,   # Target component ID
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
    # Send the message
    master.mav.send(msg)
    print(f"Message sent {msg}")

    # Wait for a short interval
    time.sleep(1)
