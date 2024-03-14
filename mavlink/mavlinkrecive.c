#include <stdio.h>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib")

#define SYSID 1
#define COMPID 154 // Assuming Gimbal component
#define PORT 14550
#define BUFLEN 1024

int main() {
    WSADATA wsa;
    SOCKET s;
    struct sockaddr_in server, si_other;
    int slen = sizeof(si_other);
    char buf[BUFLEN];

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("Failed. Error Code : %d", WSAGetLastError());
        return 1;
    }

    // Create a socket
    if ((s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == INVALID_SOCKET) {
        printf("Could not create socket : %d", WSAGetLastError());
    }

    // Prepare the sockaddr_in structure
    memset(&server, 0, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(PORT);

    // Bind
    if (bind(s, (struct sockaddr *)&server, sizeof(server)) == SOCKET_ERROR) {
        printf("Bind failed with error code : %d", WSAGetLastError());
        return 1;
    }

    while (1) {
        // Receive data
        if (recvfrom(s, buf, BUFLEN, 0, (struct sockaddr *)&si_other, &slen) == SOCKET_ERROR) {
            printf("recvfrom() failed with error code : %d", WSAGetLastError());
        }

        // Print received data in hexadecimal format
        printf("Received packet from %s:%d\nData (hex): ", inet_ntoa(si_other.sin_addr), ntohs(si_other.sin_port));
        for (int i = 0; i < slen; i++) {
            printf("%02X ", (unsigned char)buf[i]);
        }
        printf("\n\n");
    }

    closesocket(s);
    WSACleanup();
    return 0;
}
