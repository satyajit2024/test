from pymavlink import mavutil
import time

# Set the ngrok tunnel URL and port
ngrok_url = '0.tcp.in.ngrok.io'
ngrok_port = '17531'

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
    print(f"MAVLink message sent{msg}")


# Main loop to send messages periodically
while True:
    send_mavlink_message()
    time.sleep(2)  # Send every 5 seconds
