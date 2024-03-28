from pymavlink import mavutil

# Start a connection listening on a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14550')

while True:
    # Wait for a message
    received_msg = the_connection.recv_msg()

    # Print the type of the received message
    if received_msg:
        print(f"Received message type: {received_msg.get_type()}")
