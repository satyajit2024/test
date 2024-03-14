#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#define PORT 5005
#define SERVER_IP "127.0.0.1"

int inet_pton(int af, const char *src, void *dst) {
    struct sockaddr_in sa;
    int result = inet_pton(af, src, &(sa.sin_addr));
    if (result == 1) {
        memcpy(dst, &(sa.sin_addr), sizeof(struct in_addr));
    }
    return result;
}

int main() {
    WSADATA wsa;
    SOCKET sockfd;
    struct sockaddr_in server_addr;
    int n;
    char *message = "Hello, Python UDP Server!";
    
    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) {
        printf("Failed to initialize Winsock\n");
        return 1;
    }

    // Create a UDP socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd == INVALID_SOCKET) {
        printf("Socket creation failed\n");
        WSACleanup();
        return 1;
    }

    // Print the message before sending it
    printf("Sending message to Python UDP Server: %s\n", message);

    // Fill server information
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    if (inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr) != 1) {
        printf("Invalid address format\n");
        closesocket(sockfd);
        WSACleanup();
        return 1;
    }

    // Send message to server
    n = sendto(sockfd, message, strlen(message), 0, (const struct sockaddr *)&server_addr, sizeof(server_addr));
    if (n == SOCKET_ERROR) {
        printf("Failed to send message: %d\n", WSAGetLastError());
        closesocket(sockfd);
        WSACleanup();
        return 1;
    }

    printf("Sent %d bytes to the server\n", n);
    printf("Message sent successfully\n");

    // Close the socket and clean up Winsock
    closesocket(sockfd);
    WSACleanup();

    return 0;
}
