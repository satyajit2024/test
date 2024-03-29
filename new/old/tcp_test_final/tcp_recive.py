import socket

TCP_IP = "0.0.0.0"
RECEIVE_PORT = 14550

# Create a TCP socket for receiving
receive_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receive_sock.bind((TCP_IP, RECEIVE_PORT))
receive_sock.listen(1)  # Listen for incoming connections

print(f"Waiting for a connection on {TCP_IP}:{RECEIVE_PORT}")

while True:
    # Accept incoming connection
    conn, addr = receive_sock.accept()
    print(f"Connected by {addr}")

    # Receive data from the client
    data = conn.recv(1024)
    if not data:
        break  # Exit loop if no more data is received

    message = data.decode('utf-8')
    print(f"Received message: {message}")

    # Perform actions based on the received data here
    # For demonstration, let's echo the message back to the client

    # Send a response back to the client
    response = f"Message Received ThankYou Client"
    conn.sendall(response.encode('utf-8'))

    # Close the connection
    conn.close()

receive_sock.close()  # Close the receiving socket after exiting the loop
