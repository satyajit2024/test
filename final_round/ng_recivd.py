import socket
from pymavlink import mavutil

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen(1)

print("MAVLink server listening...")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")

# Create a MAVLink connection over the TCP socket
master = mavutil.mavlink_connection(f'tcp:127.0.0.1:5000')
print("Connection successful")

while True:
    msg = master.recv_match(blocking=True)
    if msg:
        print("Received message:", msg)
    else:
        print("No message received")
