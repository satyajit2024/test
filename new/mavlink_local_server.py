from coapthon.server.coap import CoAP
import logging

logging.basicConfig(level=logging.INFO)

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        logging.info(f"CoAP server started at {host}:{port}")

    def render_POST(self, request):
        try:
            # Assume the payload contains a MAVLink message (encoded as bytes)
            mavlink_msg_bytes = request.payload
            logging.info(f"Received MAVLink message: {mavlink_msg_bytes}")
            return self
        except Exception as e:
            logging.error(f"Error processing POST request: {e}")
            return self

if __name__ == '__main__':
    server = CoAPServer("127.0.0.1", 5683)  # Listen on localhost
    try:
        server.listen(10)
    except KeyboardInterrupt:
        logging.info("Server Shutdown")
        server.close()
        logging.info("Exiting...")
