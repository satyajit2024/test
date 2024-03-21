import socket
import time

TCP_IP = '0.tcp.in.ngrok.io'  # Ngrok TCP tunnel address
TCP_PORT = 19196              # Ngrok assigned TCP port

# Data to be sent
message = "Hello, Cloud VM!"

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the remote server
    client_socket.connect((TCP_IP, TCP_PORT))

    # Send data and receive echoed response
    client_socket.send(message.encode())
    print(f"Sent data: {message}")

    # Receive the echoed response
    data = client_socket.recv(1024)
    print(f"Received echoed data: {data.decode()}")

except KeyboardInterrupt:
    print("KeyboardInterrupt: Stopping the loop.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the socket connection
    client_socket.close()
