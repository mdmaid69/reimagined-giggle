import os
def get_file_size(filename):
        return os.path.getsize(filename)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()