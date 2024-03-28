import socket
from pymavlink import mavutil
import time

mav_conn = mavutil.mavlink_connection('tcpin:localhost:14550')  
print("Waiting For message.....")

sending_mode = False  # Flag to indicate whether to send messages
def send_mavlink_message():
    msg = mav_conn.mav.command_long_encode(
        0, 0,  # target system, target component
        mavutil.mavlink.MAV_CMD_USER_1,  # command
        0,  # confirmation
        1,  # param1
        0,  # param2
        0,  # param3
        0,  # param4
        0,  # param5
        0,  # param6
        0)  # param7
    mav_conn.mav.send(msg)
    print(f"MAVLink message sent{msg}") 

while True:
    if not sending_mode:
        msg = mav_conn.recv_match()
        if msg:
            print('Received:', msg)
            sending_mode = True  # Switch to sending mode

    if sending_mode:
        # Example: Send a heartbeat message (message ID 0)
        while True:
            send_mavlink_message()
            print('Sent heartbeat message')
            time.sleep(2)
        # Optionally, you can add more code here to send additional messages as needed

    # mav_conn.close()
    # print('Connection closed')
    # break  # Exit the loop after sending message


