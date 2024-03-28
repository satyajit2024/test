from coapthon.client.helperclient import HelperClient

client = HelperClient(server=('98.70.76.242', 5683))

response = client.get('hello/')
print("Response Code:", response.code)
print("Response Payload:", response.payload)

client.stop()
