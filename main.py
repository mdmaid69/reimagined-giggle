import os
def list_files_in_directory(path):
        return os.listdir(path)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()