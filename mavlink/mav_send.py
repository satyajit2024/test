from pymavlink import mavutil
import time

# Create a connection (UDP in this case)
connection = mavutil.mavlink_connection('udp:localhost:14550')

# Create a MAVLink message object (e.g., HEARTBEAT)
# You can choose the appropriate message type based on your use case
heartbeat = mavutil.mavlink.MAVLink_heartbeat_message(
    mavutil.mavlink.MAV_TYPE_GCS,
    mavutil.mavlink.MAV_AUTOPILOT_INVALID,
    mavutil.mavlink.MAV_MODE_MANUAL_ARMED,
    0,
    mavutil.mavlink.MAV_STATE_ACTIVE,
    mavlink_version=3  # Specify the MAVLink version
)

while True:
    try:
        # Send the MAVLink message
        connection.mav.send(heartbeat)
        print(heartbeat)
        # Wait for a short duration before sending the next heartbeat
        time.sleep(1)
    except KeyboardInterrupt:
        break
