from pymavlink import mavutil
import time

# Start a connection listening on a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14550')

# Set the parameters for the HEARTBEAT message
heartbeat_params = (6, 8, 192, 0, 3, 0)

while True:
    # Create a HEARTBEAT message without sending it
    heartbeat_msg = the_connection.mav.heartbeat_encode(*heartbeat_params)

    # Print the details of the message
    print(f"Sending HEARTBEAT message: {heartbeat_msg}")

    # Send the HEARTBEAT message
    the_connection.mav.send(heartbeat_msg)

    # Add a delay if needed
    time.sleep(1)
