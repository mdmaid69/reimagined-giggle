import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)