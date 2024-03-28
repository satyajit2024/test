from pymavlink import mavutil

try:
    # Create a UDP connection for sending messages
    master = mavutil.mavlink_connection('udpout:98.70.76.242:14550')

    # Example COMMAND_LONG message
    msg = master.mav.command_long_encode(
        0, 0, 0, mavutil.mavlink.MAV_CMD_NAV_LOITER_UNLIM, 0, 0, 0, 0, 0, 0, 0
    )

    if msg is not None:
        # Send the message
        master.mav.send(msg)
        print("Message sent successfully")
    else:
        print("Error: Message object is None")
except Exception as e:
    print("An error occurred:", e)
