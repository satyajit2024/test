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

try:
    while True:
        data, addr = sock.recvfrom(1024)  # Adjust buffer size as needed

        # Unpack the received data into a MAVLink object
        # msg = mavutil.mavlink.MAVLink(data, 2, 1)

        # data = data.decode("utf-8")
        # msg = mavutil.mavlink.MAVLink(data, 2, 1)
        # print(data)
        # print(type(data))

        print(data,"\n")
        

except KeyboardInterrupt:
    exit
finally:
    sock.close()
