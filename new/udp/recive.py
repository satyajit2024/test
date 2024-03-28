from pymavlink import mavutil

try:
    # Create a UDP connection for receiving messages
    master = mavutil.mavlink_connection('udpin:localhost:14550')

    while True:
        msg = master.recv_match(blocking=True)
        if msg:
            print("Received message:", msg)
            # Process the received message based on its type and content

except Exception as e:
    print("An error occurred:", e)
