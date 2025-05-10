# modules/services_info.py
import subprocess

def collect(output_folder):
    """Collect Windows services information."""
    filename = f"{output_folder}/services_info.txt"
    with open(filename, "w") as f:
        try:
            output = subprocess.check_output("sc query type= service state= all", shell=True, text=True)
            f.write(output)
        except Exception:
            f.write("Unable to query services.\n")
    print("[+] Services info collected.")
