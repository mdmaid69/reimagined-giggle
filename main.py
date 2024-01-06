import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()