# modules/yara_scanner.py
import yara
import os

def collect(output_folder):
    """Scan disk using YARA rules."""
    rules_folder = "config/yara_rules"
    scan_folder = input("\n[+] Enter path to scan: ").strip()
    output_file = f"{output_folder}/yara_scan_results.txt"

    if not os.path.exists(scan_folder):
        print("[-] Path does not exist.")
        return

    rule_files = [os.path.join(rules_folder, f) for f in os.listdir(rules_folder) if f.endswith(('.yar', '.yara'))]
    rules = yara.compile(filepaths={os.path.basename(f): f for f in rule_files})

    with open(output_file, "w") as out:
        for root, _, files in os.walk(scan_folder):
            for file in files:
                path = os.path.join(root, file)
                try:
                    matches = rules.match(path)
                    if matches:
                        out.write(f"\nMatch in {path}: {matches}\n")
                except Exception:
                    continue
    print("[+] YARA scan complete.")

