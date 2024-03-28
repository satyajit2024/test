import socket
from pymavlink import mavutil

mav_conn = mavutil.mavlink_connection('tcpin:localhost:14550')  

while True:
    msg = mav_conn.recv_match()
    if msg:
        print('Received:', msg)
        

