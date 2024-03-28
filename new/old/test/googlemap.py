import requests

def get_location(api_key, cell_towers):
    url = "https://www.googleapis.com/geolocation/v1/geolocate"
    params = {"key": api_key}
    data = {"cellTowers": cell_towers}

    response = requests.post(url, params=params, json=data)
    
    if response.status_code == 200:
        location = response.json()["location"]
        return location["lat"], location["lng"]
    else:
        print("Error:", response.status_code)
        return None

# Example usage
api_key = "YOUR_GOOGLE_MAPS_API_KEY"
cell_towers_data = [
    {"cellId": 12345, "locationAreaCode": 6789, "mobileCountryCode": 123, "mobileNetworkCode": 45}
    # Add more cell towers if needed
]

coordinates = get_location(api_key, cell_towers_data)

if coordinates:
    print("Latitude:", coordinates[0])
    print("Longitude:", coordinates[1])
else:
    print("Failed to retrieve location.")
