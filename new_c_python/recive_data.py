import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 3000
UDP_FRAME = 1442  # Adjust frame size as needed

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(UDP_FRAME)
    print(f"Received message from {addr}: {data.hex()}")
