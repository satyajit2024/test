from pymavlink import mavutil
import time

# Create MAVLink connection
mav_conn = mavutil.mavlink_connection('tcp:98.70.76.242:14550')  # Connect to the TCP server

while True:
    try:
        # Example: Send a MAVLink message (Heartbeat)
        mav_conn.mav.heartbeat_send(
            # Type of system (Ground Control Station)
            mavutil.mavlink.MAV_TYPE_GCS,
            # Autopilot type (not used here)
            mavutil.mavlink.MAV_AUTOPILOT_INVALID,
            0,  # System mode (not used here)
            0,  # Custom mode (not used here)
            0  # System state (not used here)
        )

        # Optionally, add a delay to control the message sending rate
        time.sleep(1)  # 1 second delay between messages

    except KeyboardInterrupt:   
        print("Keyboard interrupt detected. Exiting loop.")
        break
    except Exception as e:
        print("An error occurred:", str(e))

# Close the MAVLink connection
mav_conn.close()
