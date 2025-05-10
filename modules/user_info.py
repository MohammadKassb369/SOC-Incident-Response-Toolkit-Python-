# modules/user_info.py
import os
import subprocess

def collect(output_folder):
    """Collect user session and account information."""
    filename = f"{output_folder}/user_info.txt"
    with open(filename, "w") as f:
        try:
            f.write("Logged on users:\n")
            output = subprocess.check_output("query user", shell=True, text=True)
            f.write(output)
        except Exception:
            f.write("query user not available.\n")
        try:
            if os.name == 'nt':
                output = subprocess.check_output("net user", shell=True, text=True)
                f.write("\nLocal Accounts:\n")
                f.write(output)
        except Exception:
            f.write("Unable to list local accounts.\n")
    print("[+] User info collected.")
