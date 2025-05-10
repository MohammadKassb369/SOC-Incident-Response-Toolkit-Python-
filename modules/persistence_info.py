# modules/persistence_info.py
import subprocess

def collect(output_folder):
    """Collect persistence mechanisms (autoruns)."""
    filename = f"{output_folder}/persistence_info.txt"
    with open(filename, "w") as f:
        try:
            output = subprocess.check_output('reg query "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"', shell=True, text=True)
            f.write("HKLM Run Keys:\n")
            f.write(output)
        except Exception:
            f.write("Failed to read HKLM Run keys.\n")
        try:
            output = subprocess.check_output('reg query "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"', shell=True, text=True)
            f.write("\nHKCU Run Keys:\n")
            f.write(output)
        except Exception:
            f.write("Failed to read HKCU Run keys.\n")
    print("[+] Persistence info collected.")
