import psutil

def get_mac_address(interface='Ethernet'):
    try:
        mac = psutil.net_if_stats()[interface].address
    except (KeyError, psutil.Error):
        mac = None
    return mac

# Example usage
interface_name = 'Ethernet'  # replace with the desired interface name
mac_address = get_mac_address(interface_name)

if mac_address:
    print(f"MAC Address of {interface_name}: {mac_address}")
else:
    print(f"MAC Address of {interface_name} not found.")
