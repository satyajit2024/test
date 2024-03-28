import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get the IP address of the network interface connected to the client's network
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Connect to a public IP address to get the local IP
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

server_port = 5005

# Bind the socket to the server address and port
server_address = (server_ip, server_port)
server_socket.bind(server_address)
print(f"Server listening on {server_ip}:{server_port}")

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received {data.decode()} from {client_address}")

    # Send a response back to the client
    response = b"Data received successfully!"
    server_socket.sendto(response, client_address)
