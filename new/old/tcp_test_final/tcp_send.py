import socket

TCP_IP = "localhost"
RECEIVE_PORT = 14550

# Create a TCP socket for sending
send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
send_sock.connect((TCP_IP, RECEIVE_PORT))

# Send data to the server
message = "Hello, server!"
send_sock.sendall(message.encode('utf-8'))

# Receive a response from the server (optional)
response = send_sock.recv(1024)
print(f"Received response from server: {response.decode('utf-8')}")

# Close the connection
send_sock.close()
