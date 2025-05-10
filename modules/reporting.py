# modules/reporting.py
import datetime
import platform
import socket

def collect(output_folder):
    """Generate summary report."""
    filename = f"{output_folder}/triage_summary.txt"
    with open(filename, "w") as f:
        f.write("SOC Toolkit - Triage Summary Report\n")
        f.write(f"Date: {datetime.datetime.now()}\n")
        f.write(f"Host: {socket.gethostname()}\n")
        f.write(f"OS: {platform.system()} {platform.release()}\n")
    print("[+] Triage summary report generated.")
