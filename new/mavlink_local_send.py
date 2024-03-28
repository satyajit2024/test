from coapthon.client.helperclient import HelperClient
from pymavlink import mavutil
import logging

logging.basicConfig(level=logging.INFO)

def send_mavlink_message():
    # Create a MAVLink heartbeat message
    msg = mavutil.mavlink.MAVLink_heartbeat_message(
        mavutil.mavlink.MAV_TYPE_GCS,
        mavutil.mavlink.MAV_AUTOPILOT_INVALID,
        mavutil.mavlink.MAV_MODE_TEST_DISARMED,
        0,
        mavutil.mavlink.MAV_STATE_STANDBY,
        0
    )
    msg.pack(mavutil.mavlink.MAVLink('', 255, 0))  # Pack the message

    # Get the MAVLink message as bytes
    mavlink_msg_bytes = msg.get_msgbuf()

    # Send the MAVLink message over CoAP
    client = HelperClient(server=('127.0.0.1', 5683))
    client.put('mavlink/', payload=mavlink_msg_bytes, content_format=50)  # Use PUT method and content_format=50 for binary data
    client.stop()

if __name__ == '__main__':
    send_mavlink_message()
