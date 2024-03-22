import socket

# Serveo URL and port
SERVEO_URL = '20.244.107.119'
SERVEO_PORT = 5000

# Data to be sent
message = "Hello, Cloud VM!"

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Send the message
    client_socket.sendto(message.encode(), (SERVEO_URL, SERVEO_PORT))
    print(f"Sent data: {message}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the socket connection
    client_socket.close()
