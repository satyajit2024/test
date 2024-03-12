#include <stdio.h>
#include <stdlib.h>
#include <winsock2.h>
#include <mavlink/c_library_v2/mavlink.h>

#define UDP_PORT 14550

int main() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        fprintf(stderr, "WSAStartup failed\n");
        return 1;
    }

    SOCKET socket_fd;
    struct sockaddr_in sockaddr;
    mavlink_message_t msg;
    uint8_t buf[MAVLINK_MAX_PACKET_LEN];

    // Create a UDP socket
    if ((socket_fd = socket(AF_INET, SOCK_DGRAM, 0)) == INVALID_SOCKET) {
        fprintf(stderr, "Socket creation failed\n");
        WSACleanup();
        return 1;
    }

    // Configure the server address
    memset(&sockaddr, 0, sizeof(sockaddr));
    sockaddr.sin_family = AF_INET;
    sockaddr.sin_addr.s_addr = INADDR_ANY;
    sockaddr.sin_port = htons(UDP_PORT);

    // Bind the socket to the specified port
    if (bind(socket_fd, (struct sockaddr*)&sockaddr, sizeof(sockaddr)) == SOCKET_ERROR) {
        fprintf(stderr, "Socket bind failed\n");
        closesocket(socket_fd);
        WSACleanup();
        return 1;
    }

    printf("MAVLink receiver is listening on port %d\n", UDP_PORT);

    while (1) {
        // Receive data from the socket
        int sockaddr_len = sizeof(sockaddr);
        ssize_t received_bytes = recvfrom(socket_fd, buf, MAVLINK_MAX_PACKET_LEN, 0,
                                          (struct sockaddr*)&sockaddr, &sockaddr_len);

        if (received_bytes == SOCKET_ERROR) {
            fprintf(stderr, "Error receiving data\n");
            closesocket(socket_fd);
            WSACleanup();
            return 1;
        }

        // Parse the received data
        for (ssize_t i = 0; i < received_bytes; ++i) {
            if (mavlink_parse_char(MAVLINK_COMM_0, buf[i], &msg, NULL)) {
                // Message received
                printf("Received MAVLink message: ID=%d, SysID=%d, CompID=%d\n",
                       msg.msgid, msg.sysid, msg.compid);
            }
        }
    }

    // Close the socket and cleanup
    closesocket(socket_fd);
    WSACleanup();

    return 0;
}
