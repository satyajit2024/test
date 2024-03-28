from coapthon.server.coap import CoAP
from pymavlink import mavutil
import logging

logging.basicConfig(level=logging.INFO)

class MAVLinkHandler:
    def __init__(self):
        self.master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')  # MAVLink UDP connection
        self.master.wait_heartbeat()

    def send_mavlink_message(self, msg):
        try:
            self.master.mav.send(msg)
            logging.info("MAVLink message sent successfully")
        except Exception as e:
            logging.error(f"Error sending MAVLink message: {e}")

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.mavlink_handler = MAVLinkHandler()

    def render_POST(self, request):
        try:
            # Assume the payload contains a MAVLink message (encoded as bytes)
            mavlink_msg_bytes = request.payload
            # Process and validate the MAVLink message
            if self.validate_mavlink_message(mavlink_msg_bytes):
                self.mavlink_handler.send_mavlink_message(mavlink_msg_bytes)
                return self
            else:
                logging.error("Invalid MAVLink message format")
                return self
        except Exception as e:
            logging.error(f"Error processing POST request: {e}")
            return self

    def validate_mavlink_message(self, msg_bytes):
        # Add your logic to validate the MAVLink message format
        # For example, check message length, header structure, etc.
        # Return True if the message is valid, False otherwise
        return True  # Placeholder, replace with actual validation logic

if __name__ == '__main__':
    server = CoAPServer("0.0.0.0", 5683)  # Listen on all available interfaces
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")
