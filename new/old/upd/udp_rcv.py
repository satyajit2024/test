import socket

UDP_IP = "localhost"
RECEIVE_PORT = 14550

# Create a UDP socket for receiving
receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_sock.bind((UDP_IP, RECEIVE_PORT))


while True:
    # Wait for data
    data, addr = receive_sock.recvfrom(1024)
    message = data.decode('utf-8')
    print(f"Received message: {message} from {addr}")

