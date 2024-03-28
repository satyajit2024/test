from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource
import logging

logging.basicConfig(level=logging.INFO)

class HelloWorldResource(Resource):
    def __init__(self, name="HelloWorldResource", coap_server=None):
        super(HelloWorldResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=False)
        self.payload = "Hello, CoAP!"

    def render_GET(self, request):
        return self

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('hello/', HelloWorldResource())

if __name__ == '__main__':
    server = CoAPServer("127.0.0.1", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")
