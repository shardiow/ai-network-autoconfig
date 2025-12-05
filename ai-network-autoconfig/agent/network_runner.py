# agent/network_runner.py (SIMULATED FOR TESTING)

# We are intentionally leaving out 'from netmiko import ConnectHandler'

def get_running_config(device):
    """
    SIMULATED: Returns a fake running config string.
    This simulates a device that is slightly out-of-date, forcing a drift detection.
    """
    device_name = device.get('name', 'unknown_device')
    print(f"[SIMULATION] Checking current configuration on {device_name}...")
    
    # Return a basic config that WILL NOT match the desired-configs/*.cfg file
    return f"hostname {device_name}\ninterface Loopback0\nip address 1.1.1.1 255.255.255.255"

def apply_config(device, config):
    """
    SIMULATED: This pretends to push the config to the device and returns success.
    """
    device_name = device.get('name', 'unknown_device')
    print(f"[SIMULATION] SUCCESS: Config pushed to {device_name}.")
    print(f"[SIMULATION] The following config was 'applied':\n{config[:100]}...")
    # This function must not return an error for the workflow to turn green
    pass
