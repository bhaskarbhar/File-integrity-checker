import os
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    
    with open(file_path,"rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            sha256_hash.update(data)
    
    return sha256_hash.hexdigest()

def check_integrity(path):
    if os.path.isfile(path):
        # Handle file
        hash_value = calculate_sha256(path)
        if hash_value:
            print(f"File: {path}\n SHA-256: {hash_value}")
    elif os.path.isdir(path):
        # Handle directory (unchanged from original code)
        for root, dirs, files in os.walk(path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                hash_value = calculate_sha256(file_path)
                if hash_value:
                    print(f"File: {file_path}\n SHA-256: {hash_value}")
    else:
        print(f"Path {path} is not a valid file or directory")
            
if __name__=="__main__":
    directory_to_check = input("Enter the directory path to check integrity: ")
    check_integrity(directory_to_check)