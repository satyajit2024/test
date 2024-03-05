from pymavlink import mavutil

vehicle = mavutil.mavlink_connection('udp:localhost:5007')
vehicle.wait_heartbeat()

while True:
    msg = vehicle.recv_match(type='HEARTBEAT')
    if msg:
        print(f"Received message: {msg.get_type()}, {msg}")
    else:
        print("No message received")