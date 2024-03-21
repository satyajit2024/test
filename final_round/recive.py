from pymavlink import mavutil

# Receiver's IP address and port
receiver_ip = 'localhost'
receiver_port = 14550  # MAVLink default UDP port

# Create a UDP socket for receiving MAVLink messages
receiver_socket = mavutil.mavlink_connection(
    f'udp:{receiver_ip}:{receiver_port}')

# Example: Receive and print incoming MAVLink messages
while True:
    msg = receiver_socket.recv_match(blocking=True)
    if msg:
        print(f'Received message: {msg}')
