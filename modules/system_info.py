# modules/system_info.py
import platform
import socket
import datetime

def collect(output_folder):
    filename = f"{output_folder}/system_info.txt"
    with open(filename, "w") as f:
        f.write(f"Collection Time: {datetime.datetime.now()}\n")
        f.write(f"System: {platform.system()} {platform.release()}\n")
        f.write(f"Machine: {platform.machine()}\n")
        f.write(f"Processor: {platform.processor()}\n")
        f.write(f"Hostname: {socket.gethostname()}\n")
        f.write(f"IP Address: {socket.gethostbyname(socket.gethostname())}\n")
    print("[+] System info collected.")
