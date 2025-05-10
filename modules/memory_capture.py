# modules/memory_capture.py
import subprocess
import os

def collect(output_folder):
    """Capture system memory using winpmem."""
    tool = "tools/winpmem.exe"
    output_file = f"{output_folder}/memory_dump.raw"

    if not os.path.exists(tool):
        print("[-] winpmem.exe not found.")
        return

    confirm = input("[!] Memory capture can take time + space. Proceed? (Y/N): ").upper()
    if confirm != "Y":
        print("[-] Skipped memory capture.")
        return

    try:
        subprocess.run([tool, "--output", output_file], check=True)
        print(f"[+] Memory dump saved at {output_file}")
    except subprocess.CalledProcessError:
        print("[-] Memory capture failed.")
