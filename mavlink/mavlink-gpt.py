import socket
from pymavlink import mavutil
import time
import threading

# Sender function
def send_message(target_ip, target_port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    master = mavutil.mavlink_connection("udpout:{}:{}".format(target_ip,target_port))

    server_address = (target_ip,target_port)
    # Send a test message
    while True:
        msg = mavutil.mavlink.MAVLink_heartbeat_message(
            type=mavutil.mavlink.MAV_TYPE_GCS,  # or MAV_TYPE_ONBOARD_CONTROLLER if applicable
            autopilot=mavutil.mavlink.MAV_AUTOPILOT_INVALID,
            base_mode=mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            custom_mode=0,  # MAV_MODE_FLAG_TEST_ENABLED
            system_status=0,  # MAV_MODE_FLAG_AUTO_ENABLED
            mavlink_version=0,  # MAV_MODE_FLAG_GUIDED_ENABLED
        )
        data = msg.pack(mavutil.mavlink.MAVLink('', 2, 1))  # '2' is the mavlink version, '1' is the system ID
        udp_socket.sendto(data, server_address)
        print("Heart Beat Message.....",msg)
        time.sleep(1)



# Receiver function
def receive_message(bind_ip, bind_port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific IP and port
    udp_socket.bind((bind_ip, bind_port))

    print("Waiting for messages...")

    while True:
        # Receive data from the socket
        data, addr = udp_socket.recvfrom(1024)
        print(f"Received Data: {data}")

        # Create a MAVLink message from the received data
        mavlink_message = mavutil.mavlink.MAVLink(data)
        receive_message = mavlink_message.unpack()
        print(f"Received message: {receive_message}")

# Run sender and receiver in separate threads
if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Use the target IP address (localhost in this case)
    target_port = 3000  # Use the target port number

    bind_ip = "127.0.0.1"  # Use the IP address to bind the receiver socket
    bind_port = 3000  # Use the port number to bind the receiver socket

    # Create threads for sender and receiver
    sender_thread = threading.Thread(target=send_message, args=(target_ip, target_port))
    receiver_thread = threading.Thread(target=receive_message, args=(bind_ip, bind_port))

    # Start both threads
    sender_thread.start()
    receiver_thread.start()

    # Wait for both threads to finish
    sender_thread.join()
    receiver_thread.join()
