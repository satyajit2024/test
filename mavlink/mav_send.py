from pymavlink import mavutil
import time

vehicle = mavutil.mavlink_connection('udp:localhost:5007')

while True:
    try:
        vehicle.wait_heartbeat()
    except TimeoutError:
        print("Connection to vehicle lost. Reconnecting...")
        time.sleep(1)
        continue

    # Send a heartbeat message
    vehicle.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_GENERIC, 0, 0, 0)
    time.sleep(1)  # Wait for 1 second