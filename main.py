# main.py
import os
import sys
import datetime
from modules import system_info, network_info, process_info, user_info, services_info, persistence_info
from utils import create_output_folder, zip_output_folder

def show_menu():
    print("\n====== SOC Incident Response Toolkit v3 ======")
    print(f"Hostname: {os.getenv('COMPUTERNAME') or os.uname().nodename}")
    print("=============================================")
    print("1. Collect System Info")
    print("2. Collect User Info")
    print("3. Collect Network Info")
    print("4. Collect Process List")
    print("5. Collect Services Info")
    print("6. Collect Persistence Info (Autoruns)")
    print("R. Run Full Triage")
    print("Q. Quit")
    print("=============================================")

def main():
    output_folder = create_output_folder()
    while True:
        show_menu()
        choice = input("Select an option: ").upper()
        if choice == "1":
            system_info.collect(output_folder)
        elif choice == "2":
            user_info.collect(output_folder)
        elif choice == "3":
            network_info.collect(output_folder)
        elif choice == "4":
            process_info.collect(output_folder)
        elif choice == "5":
            services_info.collect(output_folder)
        elif choice == "6":
            persistence_info.collect(output_folder)
        elif choice == "R":
            system_info.collect(output_folder)
            user_info.collect(output_folder)
            network_info.collect(output_folder)
            process_info.collect(output_folder)
            services_info.collect(output_folder)
            persistence_info.collect(output_folder)
            print("\n[+] Full triage complete.")
        elif choice == "Q":
            zip_output_folder(output_folder)
            print("[+] Toolkit run complete. Exiting.")
            sys.exit()
        else:
            print("[-] Invalid selection.")

if __name__ == "__main__":
    main()
