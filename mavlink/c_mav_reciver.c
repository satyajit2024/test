#include <stdio.h>
#include <winsock2.h>
#include <string.h>

#pragma comment(lib, "ws2_32.lib")

#define PORT 14550
#define BUFLEN 1024

// Include MAVLink headers for the desired dialect/version
#include <mavlink/mavlink.h>

// Function to parse received data into MAVLink message
void parse_mavlink_message(const char* hex_data, int len) {
    mavlink_message_t msg;
    mavlink_status_t status;
    for (int i = 0; i < len; ++i) {
        if (mavlink_parse_char(MAVLINK_COMM_0, hex_data[i], &msg, &status)) {
            // Message received
            switch (msg.msgid) {
                case MAVLINK_MSG_ID_HEARTBEAT: {
                    mavlink_heartbeat_t heartbeat;
                    mavlink_msg_heartbeat_decode(&msg, &heartbeat);
                    printf("Received HEARTBEAT message:\n");
                    printf("  Type: %u\n", heartbeat.type);
                    printf("  Autopilot: %u\n", heartbeat.autopilot);
                    printf("  Base mode: %u\n", heartbeat.base_mode);
                    printf("  Custom mode: %u\n", heartbeat.custom_mode);
                    printf("  System status: %u\n", heartbeat.system_status);
                    printf("  MAVLink version: %u\n", heartbeat.mavlink_version);
                    break;
                }
                // Add cases for other MAVLink message IDs as needed
                default:
                    printf("Received unknown MAVLink message with ID: %d\n", msg.msgid);
                    break;
            }
        }
    }
}

int main() {
    WSADATA wsa;
    SOCKET s;
    struct sockaddr_in si_other;
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
        return 1;
    }

    // Prepare the sockaddr_in structure
    memset(&si_other, 0, sizeof(si_other));
    si_other.sin_family = AF_INET;
    si_other.sin_port = htons(PORT);
    si_other.sin_addr.s_addr = INADDR_ANY;

    // Bind
    if (bind(s, (struct sockaddr *)&si_other, sizeof(si_other)) == SOCKET_ERROR) {
        printf("Bind failed with error code : %d", WSAGetLastError());
        return 1;
    }

    while (1) {
        // Receive data
        int recv_len = recvfrom(s, buf, BUFLEN, 0, (struct sockaddr *)&si_other, &slen);
        if (recv_len == SOCKET_ERROR) {
            printf("recvfrom() failed with error code : %d", WSAGetLastError());
        } else {
            // Process received data
            parse_mavlink_message(buf, recv_len);
        }
    }

    closesocket(s);
    WSACleanup();
    return 0;
}
