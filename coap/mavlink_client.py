from coapthon.client.helperclient import HelperClient
from pymavlink import mavutil
import struct
import logging

logging.basicConfig(level=logging.DEBUG)  # Enable debug logging

client = HelperClient(server=('98.70.76.242', 5683))


# Create a MAVLink message (example: heartbeart message)
msg = mavutil.mavlink.MAVLink_heartbeat_message(
    mavutil.mavlink.MAV_TYPE_GCS,
    mavutil.mavlink.MAV_AUTOPILOT_INVALID,
    mavutil.mavlink.MAV_MODE_TEST_DISARMED,
    0,
    mavutil.mavlink.MAV_STATE_STANDBY,
    0
)
packed_msg = msg.pack(mavutil.mavlink.MAVLink('', 255, 0))  # Pack the message

# Convert the binary MAVLink message to a string
msg_str = struct.pack('B' * len(packed_msg), *packed_msg)

# Send the MAVLink message over CoAP
client.post('mavlink/', msg_str)

client.stop()
