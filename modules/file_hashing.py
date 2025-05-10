# modules/file_hashing.py
import os
import hashlib

def get_hashes(filepath):
    hashes = {'md5': '', 'sha1': '', 'sha256': ''}
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            hashes['md5'] = hashlib.md5(data).hexdigest()
            hashes['sha1'] = hashlib.sha1(data).hexdigest()
            hashes['sha256'] = hashlib.sha256(data).hexdigest()
    except Exception:
        pass
    return hashes

def collect(output_folder):
    """Recursively hash files in a folder."""
    folder = input("\n[+] Enter folder path to hash: ").strip()
    output_file = f"{output_folder}/file_hashes.csv"

    if not os.path.exists(folder):
        print("[-] Path does not exist.")
        return

    with open(output_file, "w") as out:
        out.write("File Path,MD5,SHA1,SHA256\n")
        for root, _, files in os.walk(folder):
            for file in files:
                path = os.path.join(root, file)
                hashes = get_hashes(path)
                if hashes['md5']:
                    out.write(f"{path},{hashes['md5']},{hashes['sha1']},{hashes['sha256']}\n")
    print("[+] File hashing complete.")
