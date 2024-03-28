#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <winsock2.h> // Use Winsock headers

#define PORT (3000)
#define SERVERADDRESS "127.0.0.1" // Change this to the server's IP address
#define BUFFER_SIZE (1000) // Adjust buffer size as needed
#define UDP_FRAME (1442) // Adjust frame size as needed

char buffer[BUFFER_SIZE];

// Populate the buffer with random data
void build(uint8_t* buffer, size_t length) {
    for (size_t i = 0; i < length; i++) {
        buffer[i] = (rand() % 255) + 1;
    }
}

int main(int argc, char** argv) {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        fprintf(stderr, "Error initializing Winsock\n");
        return EXIT_FAILURE;
    }

    SOCKET sockfd;
    struct sockaddr_in server;

    build(buffer, sizeof(buffer));

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd == INVALID_SOCKET) {
        fprintf(stderr, "Error creating socket\n");
        WSACleanup();
        return EXIT_FAILURE;
    }

    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr(SERVERADDRESS);
    server.sin_port = htons(PORT);

    for (size_t i = 0; i < BUFFER_SIZE; i += UDP_FRAME) {
        if (sendto(sockfd, (const char*)&buffer[i], UDP_FRAME, 0, (const struct sockaddr*)&server, sizeof(server)) == SOCKET_ERROR) {
            fprintf(stderr, "Error in sendto()\n");
            closesocket(sockfd);
            WSACleanup();
            return EXIT_FAILURE;
        }
    }

    printf("UDP data sent successfully!\n");

    closesocket(sockfd);
    WSACleanup();
    return EXIT_SUCCESS;
}
