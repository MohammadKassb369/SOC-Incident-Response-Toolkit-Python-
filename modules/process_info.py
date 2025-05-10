# modules/process_info.py
import psutil

def collect(output_folder):
    """Collect running process information."""
    filename = f"{output_folder}/process_info.txt"
    with open(filename, "w") as f:
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            f.write(f"{proc.info}\n")
    print("[+] Process list collected.")
