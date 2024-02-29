from pymavlink import mavutil

# Create a connection (UDP in this case)
connection = mavutil.mavlink_connection('udp:localhost:14550')

print(f"Listening on {connection.address}")

while True:
    try:
        # Wait for a MAVLink message
        msg = connection.recv_msg()

        # Check if a message is received
        if msg is not None:
            # Print the received message
            print(msg)

    except KeyboardInterrupt:
        break
