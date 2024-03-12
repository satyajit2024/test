import socket
from pymavlink import mavutil
# Define system and component IDs (change if needed)
sysid = 1
compid = mavutil.mavlink.MAV_COMP_ID_GIMBAL  # Assuming Gimbal component

# Define UDP connection details (localhost and port - change port if needed)
server_address = ("127.0.0.1", 14550)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

try:
    while True:
        data, addr = sock.recvfrom(1024)  # Adjust buffer size as needed

        # Unpack the received data into a MAVLink object
        # msg = mavutil.mavlink.MAVLink(data, 2, 1)

        data = data.decode("utf-8")
        msg = mavutil.mavlink.MAVLink(data, 2, 1)
        print(data)
        print(type(data))
        break
        

        # Access the fields of the unpacked message
        # print("Received MAVLink Message:")
        # print("Type:", msg.get_type())
        # print("Autopilot:", msg.autopilot)
        # print("Base Mode:", msg.base_mode)
        # Add more fields as needed

except KeyboardInterrupt:
    exit
finally:
    sock.close()
