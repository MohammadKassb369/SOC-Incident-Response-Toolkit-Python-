# utils.py
import os
import datetime
import zipfile

def create_output_folder():
    folder_name = f"output/Triage_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def zip_output_folder(folder_path):
    zip_file = f"{folder_path}.zip"
    with zipfile.ZipFile(zip_file, 'w') as zf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                zf.write(os.path.join(root, file),
                         os.path.relpath(os.path.join(root, file), folder_path))
    print(f"[+] Output archived at {zip_file}")
