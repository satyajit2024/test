from coapthon.client.helperclient import HelperClient

client = HelperClient(server=('127.0.0.1', 5683))

response = client.get('hello/')
print("Response Code:", response.code)
print("Response Payload:", response.payload)

client.stop()
