# modules/network_info.py
import psutil

def collect(output_folder):
    """Collect network information."""
    filename = f"{output_folder}/network_info.txt"
    with open(filename, "w") as f:
        f.write("Network Connections:\n")
        for conn in psutil.net_connections():
            f.write(f"{conn}\n")
    print("[+] Network info collected.")
