from pymavlink import mavutil
import time

# Set the ngrok tunnel URL and port
ngrok_url = '0.tcp.in.ngrok.io'
ngrok_port = '11788'

# Create a MAVLink connection over TCP via ngrok
master = mavutil.mavlink_connection(f'tcp:{ngrok_url}:{ngrok_port}')

# Function to send a MAVLink message
def send_mavlink_message():
    msg = master.mav.command_long_encode(
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
    master.mav.send(msg)
    print("MAVLink message sent")

# Main loop to switch between sending and receiving modes
sending_mode = True  # Start in sending mode
while True:
    if sending_mode:
        send_mavlink_message()
        sending_mode = False  # Switch to receiving mode after sending
        print("Switching to receiving mode...")
    else:
        # Receive one message
        while True:
            msg = master.recv_match()
            if msg:
                print('Received:', msg)
                sending_mode = True  # Switch back to sending mode after receiving
                print("Switching back to sending mode...")
    
    time.sleep(2)  # Delay before switching modes again
