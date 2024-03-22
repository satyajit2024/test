import socket

UDP_IP = "127.0.0.1"
RECEIVE_PORT = 5005
# SEND_PORT = 5006

# Create a UDP socket for receiving
receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_sock.bind((UDP_IP, RECEIVE_PORT))

# Create a UDP socket for sending
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Wait for data
    data, addr = receive_sock.recvfrom(1024)
    message = data.decode('utf-8')
    print(f"Received message: {message} from {addr}")

    # Send the received data to port 5006
    # send_sock.sendto(data, (UDP_IP, SEND_PORT))
