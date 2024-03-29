import socket
import threading

UDP_IP = "192.168.68.141"
SEND_PORT = 14550
# RECEIVE_PORT = 5006

# Create a UDP socket for sending
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create a UDP socket for receiving
# receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# receive_sock.bind((UDP_IP, RECEIVE_PORT))

# def receive_messages():
#     while True:
#         # Wait for data
#         data, addr = receive_sock.recvfrom(1024)
#         message = data.decode('utf-8')
#         print(f"Received message: {message} from {addr} \n")

# # Start a thread for receiving messages
# receive_thread = threading.Thread(target=receive_messages)
# receive_thread.start()

while True:
    # Get user input and send it
    message = input("Enter message: ")
    if message == "exit":
        send_sock.close()
        break
    send_sock.sendto(message.encode('utf-8'), (UDP_IP, SEND_PORT))
