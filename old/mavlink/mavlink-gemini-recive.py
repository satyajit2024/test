import socket
from pymavlink import mavutil
# Define system and component IDs (change if needed)
sysid = 1
compid = mavutil.mavlink.MAV_COMP_ID_GIMBAL  # Assuming Gimbal component

# Define UDP connection details (localhost and port - change port if needed)
server_address = ("localhost", 14550)
# allowed_client_ip = "192.168.0.140"

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)


while True:
    data, addr = sock.recvfrom(1024)  # Adjust buffer size as needed
    print(data, "\n")
