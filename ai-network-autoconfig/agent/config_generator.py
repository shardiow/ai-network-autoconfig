import json
from template_renderer import render_template

def generate_and_save_config(device_name, vendor, intent):
    """
    SIMULATED: Returns a fixed JSON object instead of calling the AI API.
    This allows us to test the template rendering and deployment logic.
    """
    print("[SIMULATION] Bypassing AI API call. Generating dummy JSON data.")
    
    # 1. Generate a fixed, dummy JSON object
    # This simulates what a real AI would produce based on an intent
    dummy_json_data = {
        "hostname": f"R1-DUMMY-{vendor.upper()}",
        "ip": "172.16.10.1",
        "mask": "255.255.255.0",
        "network": "172.16.10.0"
    }

    try:
        # 2. Use the generated JSON data (even though it's dummy) to fill the template
        final_config = render_template(vendor, dummy_json_data)
        
        # 3. Save the final configuration to the desired-configs folder
        desired_file = f"desired-configs/{device_name}.cfg"
        with open(desired_file, 'w') as f:
            f.write(final_config)
            
        print(f"[✓] New dummy config generated for {device_name} and saved to {desired_file}")
        
    except Exception as e:
        print(f"[!] Error processing dummy generation or rendering: {e}")
        return None

# The rest of your Python code that calls this function remains valid.
