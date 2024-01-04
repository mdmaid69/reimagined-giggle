import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import os
def remove_directory(path):
        os.rmdir(path)